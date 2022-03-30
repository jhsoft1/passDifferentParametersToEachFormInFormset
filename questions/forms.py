from django import forms
from django.forms import BaseFormSet, formset_factory

from questions.models import Question


class QuestionForm(forms.Form):
    text = forms.CharField(max_length=100)

    def __init__(self, *args, question, **kwargs):
        self.q_text = question.text
        super().__init__(*args, **kwargs)


class BaseQuestionFormSet(BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        q = kwargs['questions'][index]
        # note that instead of passing a dictionary which includes a copy
        # of the formset's `form_kwargs`, we actually return a dictionary
        # that holds a single key-value pair
        return {'question': q}


# using list to force "eager" evaluation here, since we'll be using all
# questions' data
qs = list(Question.objects.all())
# making sure that when instantiating formsets, they will be set to
# generate as many forms as we have questions (this seems hacky and there must
# be a better way to do this)
QuestionFormSet = formset_factory(QuestionForm, formset=BaseQuestionFormSet,
                                  extra=len(qs))
