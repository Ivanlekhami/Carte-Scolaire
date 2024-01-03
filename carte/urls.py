from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("<int:ecole_id>", home, name="result"),
    path("suggestion/", suggestion, name="suggestion"),
    path("apropos/", apropos, name="apropos"),
]