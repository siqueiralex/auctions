from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("alterar-senha/", views.PasswordChangeView.as_view(), name="alterar_senha"),
]
