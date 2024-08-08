
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/v1/books/', include('books.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls)
]