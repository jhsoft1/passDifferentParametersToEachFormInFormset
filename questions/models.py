from django.db import models


# https://forum.djangoproject.com/t/pass-different-parameters-to-each-form-in-formset/4040/2

class Question(models.Model):
    text = models.CharField(max_length=100)
