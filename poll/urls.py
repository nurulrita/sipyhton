from django.conf.urls import url


from . import views

urlpatterns = [
	# /poll/
    url(r'^$', views.index, name= 'index'),
    url(r'^help_me/$', views.help_me, name= 'help_me'),
    
]