from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Answer, Option, Quiz, Question
from django.contrib import messages

# Create your views here.


class QuizListView(ListView):
    model = Quiz
    template_name = "quiz/index.html"
    context_object_name = "quizzes"

    def get(self, request, *args, **kwargs):
        # Reset quiz session data
        self.reset_quiz_session(request)
        return super().get(request, *args, **kwargs)

    def reset_quiz_session(self, request):
        # Clear quiz-related session variables
        session_keys = list(request.session.keys())
        for key in session_keys:
            if (
                key.startswith("current_question_")
                or key.startswith("score_for_quiz_")
                or key == "submitted_answer"
            ):
                del request.session[key]


class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quiz/quiz_detail.html"
    context_object_name = "quiz"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        quiz = self.object
        question_index = request.session.get(f"current_question_{quiz.id}", 0)
        questions = quiz.questions.all()
        self.request.session[f"total_questions_for_quiz_{quiz.id}"] = questions.count()

        if question_index >= questions.count():
            return self.handle_quiz_completion(quiz.id)

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz = self.get_object()
        question_index = self.request.session.get(f"current_question_{quiz.id}", 0)
        questions = quiz.questions.all()

        if question_index >= questions.count():
            return self.handle_quiz_completion(quiz.id)

        current_question = questions[question_index]
        options = current_question.options.all()
        correct_answer = Answer.objects.filter(question=current_question).first()

        context["current_question"] = current_question
        context["options"] = options
        context["correct_answer_id"] = (
            correct_answer.correct_option.id if correct_answer else None
        )
        context["selected_option_id"] = self.request.session.get(
            f"selected_option_{question_index}"
        )
        context["is_answer_correct"] = self.request.session.get(
            f"answer_correct_{question_index}", False
        )

        context["question_index"] = question_index + 1
        context["total_questions"] = questions.count()
        context["show_next"] = "submitted_answer" in self.request.session

        context["quiz_icon_url"] = quiz.icon.url if quiz.icon else None
        context["quiz_title"] = quiz.title

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        quiz = self.object
        question_index = request.session.get(f"current_question_{quiz.id}", 0)
        questions = quiz.questions.all()

        if "go_back" in request.POST and question_index > 0:
            request.session[f"current_question_{quiz.id}"] = question_index - 1
            return redirect(request.path)

        selected_option_id = request.POST.get("answer")
        if not selected_option_id:
            messages.error(request, "Please select an answer.")
            return redirect(request.path)

        request.session[f"selected_option_{question_index}"] = selected_option_id
        current_question = questions[question_index]
        correct_answer = Answer.objects.filter(question=current_question).first()

        if (
            correct_answer
            and str(correct_answer.correct_option.id) == selected_option_id
        ):
            score = request.session.get(f"score_for_quiz_{quiz.id}", 0)
            request.session[f"score_for_quiz_{quiz.id}"] = score + 1

        if question_index < len(questions) - 1:
            request.session[f"current_question_{quiz.id}"] = question_index + 1
        else:
            return self.handle_quiz_completion(quiz.id)

        return redirect(request.path)

    def handle_quiz_completion(self, quiz_id):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        self.request.session["quiz_completed"] = True
        self.request.session["completed_quiz_id"] = quiz_id
        self.request.session["quiz_icon_url"] = quiz.icon.url if quiz.icon else None
        self.request.session["quiz_title"] = quiz.title
        score = self.request.session.get(f"score_for_quiz_{quiz_id}", 0)
        self.request.session[f"score_for_quiz_{quiz_id}"] = score
        return redirect("completion_page")


class CompletionPageView(View):
    def get(self, request, *args, **kwargs):
        quiz_id = request.session.get("completed_quiz_id")
        score = request.session.get(f"score_for_quiz_{quiz_id}", 0)
        total_questions = request.session.get(f"total_questions_for_quiz_{quiz_id}", 0)

        quiz_dict = {
            "icon": {"url": request.session.get("quiz_icon_url")},
            "title": request.session.get("quiz_title"),
        }

        context = {
            "score": score,
            "total_questions": total_questions,
            "quiz_id": quiz_id,
            "quiz": quiz_dict,
        }

        for key in [
            f"current_question_{quiz_id}",
            "quiz_completed",
            "completed_quiz_id",
        ]:
            request.session.pop(key, None)

        return render(request, "quiz/quiz_completion.html", context)
