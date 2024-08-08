from django.urls import path
from . import views


urlpatterns = [
    path('', views.GetPostCommentAPIView.as_view(), name='get_comments'),
    path('<int:pk>/', views.GetUpdateDeleteCommentAPIView.as_view(), name='get_delete_update_comment'),
]