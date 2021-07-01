from . import views
from django.urls import path


urlpatterns = [
    path('create/', views.MarkCreateView.as_view()),
    path('<int:pk>/delete/', views.MarkDeleteView.as_view()),

]