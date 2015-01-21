from django.shortcuts import render_to_response
from models import Problem
# Create your views here.
def list(request):
    problems = Problem.objects.all()

    return render_to_response('problem/list.html',locals())

def detail(request,id):
    problem = Problem.objects.get(id=id)
    options = problem.option.split('=.=')

    return render_to_response('problem/view.html',locals())