from django.shortcuts import render, redirect
from .models import Thread, Post
from .forms import ThreadForm
from django.contrib.auth.decorators import login_required

def is_valid(self, form):
	form.instance.author = self.request.user
	return super(self).form_valid(form)



def home(request):
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1
	context = {'num_visits': num_visits}
	return render(request, 'myblog/home.html', context)

#FFBE BOARD VIEWS
@login_required
def ffbe(request):
	threads = Thread.objects.filter(board='ffbe').order_by('thread_date')
	context = {'threads': threads}
	return render(request, 'myblog/ffbe.html', context)

def ffbetopic(request, topicid):
	thread = Thread.objects.get(id=topicid)
	posts = thread.post_set.order_by('post_time')
	context = {'thread': thread, 'posts': posts}
	return render(request, 'myblog/ffbetopic.html', context)

def new(request):
	if request.method != 'POST':
		form = ThreadForm()
	else:
		form = ThreadForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('myblog:home')

	context = {'form': form}
	return render(request, 'myblog/ffbenew.html', context)

#PYTHON BOARD VIEWS
def python(request):
	threads = Thread.objects.filter(board='python').order_by('thread_date')
	context = {'threads': threads}
	return render(request, 'myblog/python.html', context)

def pythontopic(request, topicid):
	thread = Thread.objects.get(id=topicid)
	posts = thread.post_set.order_by('post_time')
	context = {'thread': thread, 'posts': posts}
	return render(request, 'myblog/pythontopic.html', context)

# High strangeness
def highstrangeness(request):
	threads = Thread.objects.filter(board='high strangeness').order_by('thread_date')
	context = {'threads': threads}
	return render(request, 'myblog/highstrangeness.html', context)