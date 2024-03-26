from django.urls import path
from .views import ListBooks,BookDetailView,ListReview,ListGenre
urlpatterns = [
    path('genre/', ListGenre.as_view(), name='genre' ),
    path('book/', ListBooks.as_view(), name='book' ),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail' ),
    path('review/', ListReview.as_view(), name='review' ),
    path('rating/<int:rating>', ListReview.as_view(), name='rating-filter' ),
]