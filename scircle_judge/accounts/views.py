# coding: utf-8
from django.shortcuts import render,render_to_response,HttpResponseRedirect,RequestContext
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.db.models import Q
from accounts.models import User
from forms import LoginForm
from ipdb import set_trace
# Create your views here.
def home(request):
    if not request.user.is_active:
        return render_to_response("accounts/landing.html", locals())
    return render_to_response("accounts/dashboard.html", locals())

def login(request):
    return render_to_response("accounts/login.html", locals())

def login(request):



    if 'username' not in request.POST:
        form = LoginForm()
        return render_to_response('accounts/login.html', locals(), context_instance = RequestContext(request))
    else:
        form = LoginForm(request.POST)

    username = request.POST['username']
    password = request.POST['password']
    users = User.objects.filter(Q(email = username)| Q(username = username))
    if len(users) == 0:
        username_errors =  u"账号不存在"
        return render_to_response('accounts/login.html', locals(), context_instance = RequestContext(request))

    user = authenticate(username = users[0].username, password = password)
    if user is None:
        password_errors = u"密码错误"
        return render_to_response('accounts/login.html', locals(), context_instance = RequestContext(request))

    if not user.is_active:
        username_errors = u"该账号被冻结，请与管理员联系，谢谢。"
        return render_to_response('accounts/login.html', locals(), context_instance = RequestContext(request))

    django_login(request, user)
    if 'remember' not in request.POST:
        request.session.set_expiry(0)


    next = request.GET.get('next', '')
    if next == '':
        next = '/'

    return HttpResponseRedirect(next)



def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')