from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import unauthenticated_user
from django.contrib.auth.views import (
    LoginView as AuthLoginView,
    PasswordChangeView as AuthPasswordChangeView,
    LogoutView as AuthLogoutView,
)


@method_decorator(unauthenticated_user, name="dispatch")
class LoginView(AuthLoginView):
    template_name = "custom_auth/login.html"
    success_url = "/"

    def form_valid(self, form):
        http_respose = super().form_valid(form)
        if form.get_user().change_password:
            return redirect("alterar_senha")
        return http_respose


@method_decorator(login_required(login_url="login"), name="dispatch")
class LogoutView(AuthLogoutView):
    success_url = "/"


@method_decorator(login_required(login_url="login"), name="dispatch")
class PasswordChangeView(AuthPasswordChangeView):
    template_name = "custom_auth/alterar_senha.html"

    def form_valid(self, form):
        http_respose = super().form_valid(form)

        form.user.change_password = False
        form.user.save()

        return http_respose