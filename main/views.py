from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from main.models import AnimalImage, AdvUser
from main.forms import ChangeUserInfoForm, RegisterUserForm
from main.petsrequests import CatRequest, DoqRequest


@login_required
def profile(request):
    return render(request, 'profile.html')


def index(request):
    return render(request, 'index.html')


def cats_page(request):
    cats = CatRequest()
    context = {
        'cats_url': cats.url,
        'cats_ext': cats.ext,
        'cats_save': False,
    }
    return render(request, 'cats.html', context)


def dogs_page(request):
    dogs = DoqRequest()
    context = {
        'dogs_url': dogs.url,
        'dogs_ext': dogs.ext,
        'dogs_save': False,
    }
    return render(request, 'dogs.html', context)


def other_page(request, page):
    try:
        template = get_template(page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


def cat_save(request):
    img = AnimalImage()
    img.user = AdvUser.objects.get(pk=request.user.pk)
    img.animal_type = request.POST['pet_type']
    img.pic_url = request.POST['pet_url']
    img.file_type = request.POST['pet_ext']
    img.save()
    context = {
        'cats_url': request.POST['pet_url'],
        'cats_ext': request.POST['pet_ext'],
        'cats_save': True,
    }
    return render(request, 'cats.html', context)


def dog_save(request):
    img = AnimalImage()
    img.user = AdvUser.objects.get(pk=request.user.pk)
    img.animal_type = request.POST['pet_type']
    img.pic_url = request.POST['pet_url']
    img.file_type = request.POST['pet_ext']
    img.save()
    context = {
        'dogs_url': request.POST['pet_url'],
        'dogs_ext': request.POST['pet_ext'],
        'dogs_save': True,
    }
    return render(request, 'dogs.html', context)


def pet_delete(request):
    pic_id = request.POST['pic_id']
    pic_inst = AnimalImage.objects.get(pk=pic_id)
    pic_inst.delete()
    return redirect('main:pets_list')


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'delete_user.html'
    success_url = reverse_lazy('main:index')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'User deleted')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'User data has been changed'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'register_done.html'


class UserPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'User password changed'


class UserLogOutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


class UserLoginView(LoginView):
    template_name = 'login.html'


class PetsListListView(LoginRequiredMixin, ListView):
    model = AnimalImage
    template_name = 'pets_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.request.user.id)
        return queryset

