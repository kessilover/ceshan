from django import forms
from django.contrib.auth.models import User
from .models import Chapter,Comment,Story




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ['title', 'summary', 'tags', 'rating']


class ChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ['chapter']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment', 'writer']

