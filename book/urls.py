from django.urls import path
from book import views

urlpatterns = [
    path('reviews/', views.BookListCreateView.as_view()),
    path('review/<int:pk>/', views.BookDetailView.as_view()),

    ]
