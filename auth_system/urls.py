from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register_view, name="register-form"),
    path('login/', login_view, name="login-form"),
    path('logout/', logout_view, name="logout-form")
]