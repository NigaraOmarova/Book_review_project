from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('activate/<uuid:activation_code>', views.ActivationView.as_view(), name='activation_code'),
    path('refresh/', TokenRefreshView.as_view())
]