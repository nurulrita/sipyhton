from django.shortcuts import render

# Create your views here.
def index(request):
	context = {}
	return render(request, 'poll/index.html', context)

def help_me(request):
	context = {}
	return render(request, 'poll/help_me.html', context)