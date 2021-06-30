
from django.urls import path
from . import views


urlpatterns = [

    path('like/', views.LikeListView.as_view()),
    path('like/create/', views.LikeCreateView.as_view()),
    path('like/<int:pk>/delete/', views.LikeDeleteView.as_view()),

]