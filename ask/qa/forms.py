from django.contrib.auth.models import User

from .models import Answer, Question
from django import forms


class AskForm(forms.Form):
  title = forms.CharField(min_length=1)
  text = forms.CharField(min_length=1, widget=forms.Textarea)

  def __init__(self, user=None, **kwargs):
    self._user = user
    super(AskForm, self).__init__(**kwargs)

  # def __init__(self, *args, **kwargs):
  #   super(AskForm, self).__init__(*args, **kwargs)

  def save(self):
    # self.cleaned_data['author'] = self.user
    # self.cleaned_data['author'] = '1'
    # return Question.objects.create(**self.cleaned_data)
    question = Question(**self.cleaned_data)
    question.author_id = 1
    question.save()
    return question

class AnswerForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea)
  question = forms.ModelChoiceField(queryset=Question.objects.all())

  def __init__(self, user=None, **kwargs):
    self._user = user
    super(AnswerForm, self).__init__(**kwargs)

  # def __init__(self, *args, **kwargs):
  #   super(AnswerForm, self).__init__(*args, **kwargs)

  # def clean(self):
  #   cleaned_data = super(AnswerForm, self).clean()

  # def save(self):
  #   self.cleaned_data['author'] = self.user
  #   return Answer.objects.create(**self.cleaned_data)
  def save(self):
    self.cleaned_data["author"] = self.user
    answer = Answer(**self.cleaned_data)
    answer.save()
    return answer


class SignupForm(forms.Form):
  username = forms.CharField(min_length=1)
  email = forms.EmailField(required=False)
  password = forms.CharField(min_length=1, widget=forms.PasswordInput)

  def save(self):
    user = User.objects.create_user(**self.cleaned_data)
    user.save()
    return user


class LoginForm(forms.Form):
  username = forms.CharField(min_length=1)
  password = forms.CharField(min_length=1, widget=forms.PasswordInput)
