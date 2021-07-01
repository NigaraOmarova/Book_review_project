from django.urls import path
from category import views


urlpatterns = [
    path('list/', views.CategoryView.as_view()),
    path('create/', views.CategoryCreateView.as_view()),
    path('detail/<pk>', views.CategoryDetailView.as_view()),
]
