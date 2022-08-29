from django.contrib import admin
from django.urls import path

from .views import  BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView 

app_name='appMensajeria'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', BlogListView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
    
]