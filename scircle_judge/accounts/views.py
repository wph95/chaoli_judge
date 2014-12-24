from django.shortcuts import render,render_to_response
# Create your views here.
def home(request):
    if not request.user.is_active:
        return render_to_response("accounts/landing.html", locals())
    return render_to_response("accounts/dashboard.html", locals())