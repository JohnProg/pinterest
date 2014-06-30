from django.contrib.auth.forms import PasswordResetForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.views.generic import FormView, TemplateView

from .forms import UserForm
from .forms import UserLoginForm


class RegisterFormView(FormView):
    template_name = "myuser/home.html"
    form_class = UserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        user = form.save()
        user = authenticate(username=user.username, password=self.request.POST['password1'])
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    template_name = "myuser/home.html"
    form_class = UserLoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        return super(LoginFormView, self).form_valid(form)


class HomeTemplateView(TemplateView):
    template_name = "myuser/home.html"
    success_url = reverse_lazy('home')


class PasswordResetFormView(FormView):
    template_name = "myuser/home.html"
    form_class = PasswordResetForm
    success_url = reverse_lazy('home')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('../home')
