from django.shortcuts import render

from .models import Question

# Create your views here.
def index(request):
	context = {}
	questions_query = Question.objects.all()
	context ['questions'] = questions_query
	return render(request, 'poll/index.html', context)

def help_me(request):
	context = {}
	return render(request, 'poll/help_me.html', context)

def detail_question(request, question_id):
	context ={}
	question = Question.objects.get(id=question_id)
	context ['question'] = question
	return render (request, 'poll/detail_question.html', context)
