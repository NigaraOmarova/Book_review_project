from django.urls import path
from book import views

urlpatterns = [
    path('reviews/', views.BookListCreateView.as_view()),
    path('review/<int:pk>/', views.BookDetailView.as_view()),
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
    path('review/create/', views.BookReviewCreateView.as_view()),
    path('favorite/list/', views.FavoritesListView.as_view()),
    path('favorite/<int:pk>/delete/', views.FavoritesDeleteView.as_view()),
    path('favorite/create/', views.FavoritesCreateView.as_view()),


    ]
