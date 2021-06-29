from . import views
from django.urls import path


urlpatterns = [
    path('mark/create/', views.MarkCreateView.as_view()),
    path('mark/<int:pk>/delete/', views.MarkDeleteView.as_view()),

]