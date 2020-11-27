from django.urls import path, include
from .views import index, produto

urlpatterns = [
    path('', index, name='index'),
    path('produto/<int:pk>', produto, name='produto'),
]