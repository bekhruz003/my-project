from django.urls import path
from .views import CreateBookview, MainView, UpdateBookView, BookDetailView, BookDeleteView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('create/', CreateBookview.as_view(), name='create'),
    path('update/<int:pk>/', UpdateBookView.as_view(), name='update'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete')
]