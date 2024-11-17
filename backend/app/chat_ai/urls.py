from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'', TalesModelViewSet, basename='tales')

urlpatterns = [
    path('', include(router.urls)),
    path('top_tales/', TopTalesListView.as_view(), name='top-tales-list'),
    path('top_tales/<int:pk>/', TopTalesDetailView.as_view(), name='top-tales-detail'),
]