from django.conf.urls import url



from . import views

urlpatterns = [
	# /poll/
    url(r'^$', views.index, name= 'index'),
    url(r'^help_me/$', views.help_me, name= 'help_me'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail_question, name='detail_question'),
    
]

