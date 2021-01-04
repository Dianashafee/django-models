from django.urls import path, include
from .views import HomeView, BlogDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>', BlogDetailsView.as_view(), name='blog_details'),
]