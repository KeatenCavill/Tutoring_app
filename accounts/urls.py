from django.contrib.auth.views import LoginView
from django.urls import path
from .views import SignUpView, TutorListView, TutorDetailView, MyProfileView, EditProfileView 
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("", TutorListView.as_view(), name="home"),
    path("tutor/<int:pk>/", TutorDetailView.as_view(), name="tutor-detail"),  
    path("me/", MyProfileView.as_view(), name='my_profile'),
    path("me/edit/", EditProfileView.as_view(), name="edit_profile"),
]