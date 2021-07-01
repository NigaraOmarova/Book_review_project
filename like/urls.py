
from django.urls import path
from . import views


urlpatterns = [

    path('', views.LikeListView.as_view()),
    path('create/', views.LikeCreateView.as_view()),
    path('<int:pk>/delete/', views.LikeDeleteView.as_view()),

]