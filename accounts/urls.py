from django.urls import include, path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
  path('accounts/', include('django.contrib.auth.urls')),
]
