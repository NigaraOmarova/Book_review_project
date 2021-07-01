from django.urls import path
from chatroom import views

urlpatterns = [
    path('message/create/', views.MessagesCreateView.as_view()),
    path('', views.ChatroomListCreateView.as_view()),
    path('<int:pk>/', views.ChatroomDetailView.as_view()),
    ]
