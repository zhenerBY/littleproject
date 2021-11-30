from django.contrib.auth.views import LoginView
from django.shortcuts import render

from main.models import AnimalImage


def index(request):
    return render(request, 'index.html')


class UserLoginView(LoginView):
    template_name = 'login.html'