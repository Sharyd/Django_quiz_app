from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import QuizDetailView, QuizListView, CompletionPageView


urlpatterns = [
    path("", QuizListView.as_view(), name="home-page"),
    path("quiz/<int:pk>/", QuizDetailView.as_view(), name="quiz_detail"),
    path(
        "quiz/<int:pk>/submit-answer/", QuizDetailView.as_view(), name="submit_answer"
    ),
    path("quiz/completion/", CompletionPageView.as_view(), name="completion_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
