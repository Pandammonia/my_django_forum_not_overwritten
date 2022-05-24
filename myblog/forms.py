from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
	class Meta:
		model = Thread
		fields = ['thread_title', 'thread_body', 'board']
		labels = {'thread_title': '','thread_body': '', 'board':'Post to which board?'}

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['post_body']
		labels = {'post_body': '  '}
		widgets = {'post_body': forms.Textarea(attrs={'cols': 80})}



