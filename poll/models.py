from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    creation_date = models.DateField(auto_now=True)


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )