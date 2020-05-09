from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('event/', views.event, name='event'),
	path('success/', views.success, name='success'),
	path('fail/', views.fail, name='fail'),
	path('test/', views.check, name='check')
]