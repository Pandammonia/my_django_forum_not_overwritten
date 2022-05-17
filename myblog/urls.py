from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.home, name='home'),
    #FFBE forums
    path('ffbe/', views.ffbe, name='ffbe'),
    path('ffbe/<int:topicid>/', views.ffbetopic, name='ffbetopic'),
    #FFBE new thread
    path('ffbe/new_topic/', views.ffbenew, name='ffbenew'),
    path('python/', views.python, name='python'),
]