from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.home, name='home'),
    #FFBE forums
    path('ffbe/', views.ffbe, name='ffbe'),
    path('ffbe/<int:topicid>/', views.ffbetopic, name='ffbetopic'),
    #FFBE new thread
    path('new_topic/', views.new, name='new'),
    path('python/<int:topicid>/', views.pythontopic, name='pythontopic'),
    path('python/', views.python, name='python'),
    #High Strangeness links
    path('highstrangeness/', views.highstrangeness, name='highstrangeness'),
]