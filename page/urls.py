from django.urls import path
from .views import *
from accounts.views import *

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("administrate/", administrate, name="administrate"),
]