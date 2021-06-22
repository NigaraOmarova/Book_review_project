from django.urls import path
from category import views


urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
]