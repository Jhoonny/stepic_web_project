from .models import Answer, Question
from django import forms


class AskForm(forms.Form):
  title = forms.CharField(max_length=255)
  text = forms.CharField(widget=forms.Textarea)

  def __init__(self, user=None, **kwargs):
    self.user = user
    super(AskForm, self).__init__(kwargs)

  def clean(self):
    cleaned_data = super(AskForm, self).clean()

  def save(self):
    self.cleaned_data['author'] = self.user
    return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea)
  question = forms.ModelChoiceField(queryset=Question.objects.all())

  def __init__(self, user=None, **kwargs):
    self.user = user
    super(AnswerForm, self).__init__(kwargs)

  def clean(self):
    cleaned_data = super(AnswerForm, self).clean()

  def save(self):
    self.cleaned_data['author'] = self.user
    return Answer.objects.create(**self.cleaned_data)
