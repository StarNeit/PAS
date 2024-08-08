from django.urls import path
from . import views


urlpatterns = [
    path('', views.GetPostBookAPIView.as_view(), name='get_books'),
    path('<int:pk>/', views.GetUpdateDeleteBookAPIView.as_view(), name='get_delete_update_book'),
]