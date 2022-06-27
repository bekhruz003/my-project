from django.urls import path
from .views import CreateBookview, HomeView, UpdateBookView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('create/', CreateBookview.as_view(), name='create'),
    path('update/<int:pk>/', UpdateBookView.as_view(), name='update')
]