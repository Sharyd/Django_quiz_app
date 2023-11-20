from django.db import models
from django.core.exceptions import ValidationError
import os

# Create your models here.


def validate_file_type(upload):
    ext = os.path.splitext(upload.name)[1]
    valid_extensions = [".svg", ".jpg", ".png", ".jpeg"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    icon = models.FileField(
        upload_to="uploads/quiz_icons/", validators=[validate_file_type]
    )

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Option(models.Model):
    question = models.ForeignKey(
        Question, related_name="options", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    correct_option = models.ForeignKey(
        Option, related_name="correct_for", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Correct answer for '{self.question}': {self.correct_option.text}"
