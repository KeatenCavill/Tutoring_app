from django.contrib.auth.views import LoginView
from django.urls import path
from .views import SignUpView, TutorListView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("", TutorListView.as_view(), name="home"),
]