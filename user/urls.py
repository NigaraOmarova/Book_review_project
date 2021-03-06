from django.conf.urls import url
from django.urls import path, include

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('list/', views.UserListView.as_view()),
    path('detail/<int:pk>/', views.UserDetailView.as_view()),
    path('update/<int:pk>/', views.UserUpdateView.as_view()),
    path('delete/<int:pk>/', views.UserDestroyView.as_view()),
    path('register/', views.RegisterApiView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('activate/<uuid:activation_code>', views.ActivationView.as_view(), name='activation_code'),
    path('refresh/', TokenRefreshView.as_view()),
    path('password_reset/', views.PasswordResetApiView.as_view()),
    path('change_password/', views.NewPasswordApiView.as_view()),
]
