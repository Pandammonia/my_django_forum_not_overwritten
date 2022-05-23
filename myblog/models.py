from django.db import models
from django.contrib.auth.models import User

board_choice = [
('python', 'Python'),
('ffbe', 'FFBE'),
('high strangeness', 'High Strangeness')
]

class Thread(models.Model):
	"""Class for project information"""
	thread_title = models.CharField(max_length=120)
	thread_body = models.TextField()
	thread_date = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(blank=True, null=True)
	board = models.CharField(max_length=24, choices=board_choice, default='python')
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__ (self):
		return self.thread_title

	class Meta:
		ordering = ["thread_date"]

class Post(models.Model):
	posts_thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
	post_body = models.TextField()
	post_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.post_body[:50]




# Create your models here.
