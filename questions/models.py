from django.db import models
from django.db.models import DO_NOTHING


# https://forum.djangoproject.com/t/pass-different-parameters-to-each-form-in-formset/4040/2


class Question(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        print(f'{self.text}')


class Answer(models.Model):
    text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=DO_NOTHING)

    def __str__(self):
        print(f'{self.text} {self.question}')
