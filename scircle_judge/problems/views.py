from django.shortcuts import render_to_response
from models import Problem
# Create your views here.
def index(request):
    problem = Problem.objects.get(id=1)
    options = problem.option.split('=.=')

    return render_to_response('problem/list.html',locals())
