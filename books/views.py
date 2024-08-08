from django.shortcuts import render

from comments.serializers import CommentSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .permissions import IsOwnerOrReadOnly
from .serializers import BookSerializer
from .filters import BookFilter


class GetPostBookAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GetUpdateDeleteBookAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
