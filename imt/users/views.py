from urllib import request
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from main.models import Dish

from .models import Profile
from .forms import ProfileUpdateForm,UserCreationForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django.contrib.auth.models import User

from django.views import View

from django.contrib.auth import authenticate,login




class Register(View):

    template_name='registration/register.html'

    def get(self,request):
        context={
            'form':UserCreationForm
        }
        return render(request,self.template_name,context)
    
    def post(self,request):
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
        context={
            'form':form
        }
        return render(request,self.template_name,context)
    


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('users:profile_update')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile_update.html', context)



class ProfileView(LoginRequiredMixin,DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'users/profile.html'
    pk_url_kwarg='user_pk'

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    model = Profile
    template_name = 'users/profile_update.html'
    pk_url_kwarg = 'user_pk'
    
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.kwargs['user_pk'])
        if user != request.user:
            return HttpResponseForbidden()
        else:
            return super(UpdateProfileView, self).get(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse('profile_update', kwargs={'user_pk': self.kwargs['user_pk']})
