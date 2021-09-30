from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User

from django_social_app.forms import CreatePersonForm, CreateUserForm


def create_user(request):
    data = {}
    form = CreatePersonForm(request.POST or None)
    data['form'] = form
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        user_form = CreateUserForm(request.POST or None, instance=user)
    else:
        user_form = CreateUserForm(request.POST or None)
    data['user_form'] = user_form
    if request.POST:
        if form.is_valid() and user_form.is_valid:
            instance = user_form.save(commit=False)
            obj = form.save(commit=False)
            obj.user = instance
            instance.save()
            obj.save()
            return redirect('home')
    return render(request, 'registration/create_user.html', data)

