from django.urls import path
from .views import *
from accounts.views import *

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("<int:ecole_id>", home, name="result"),
    path("logout/", logout_user, name="logout"),
    path("administrate/", administrate, name="administrate"),
    path("suggestion/", suggestion, name="suggestion"),
    path("apropos/", apropos, name="apropos"),
    path("ajout_etab/", ajout_etab, name="ajout_etab"),
    path("modifier/<int:ecole_id>", modifier, name="modifier"),
    path("modifier_admin/<int:admin_id>", modifier_admin, name="modifier_admin"),
    path("delete_admin/<int:admin_id>", delete_admin, name="delete_admin"),
    path("delete_suggestion/<int:sug_id>", delete_suggestion, name="delete_suggestion"),
    path("desactiver/<int:ecole_id>", desactiver , name="desactiver"),
    path("activer/<int:ecole_id>", activer , name="activer"),
]