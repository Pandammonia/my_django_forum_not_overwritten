from django.shortcuts import render, redirect
from .models import Thread, Post
from .forms import ThreadForm
def home(request):
	return render(request, 'myblog/home.html')

def ffbe(request):
	threads = Thread.objects.order_by('thread_date')
	context = {'threads': threads}
	return render(request, 'myblog/ffbe.html', context)

def ffbetopic(request, topicid):
	thread = Thread.objects.get(id=topicid)
	posts = thread.post_set.order_by('post_time')
	context = {'thread': thread, 'posts': posts}
	return render(request, 'myblog/ffbetopic.html', context)

def ffbenew(request):
	if request.method != 'POST':
		form = ThreadForm()
	else:
		form = ThreadForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('myblog:ffbe')

	context = {'form': form}
	return render(request, 'myblog/ffbenew.html', context)


def python(request):
	return render(request, 'myblog/python.html')

# Create your views here.
