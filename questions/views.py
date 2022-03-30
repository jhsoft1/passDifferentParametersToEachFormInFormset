from django.shortcuts import render

from questions.forms import QuestionFormSet, qs


def manage_questions(request):
    if request.method == 'POST':
        formset = QuestionFormSet(data=request.POST)
        if formset.is_valid():
            formset.save()
            # do something
    else:
        formset = QuestionFormSet(form_kwargs={'questions': qs})
        print('0 ', formset.forms[0].q_text)
    return render(request, "questions/manage_questions.html", {"formset": formset})
