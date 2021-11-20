from django.urls import path, include
from store.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Cuatomers', views.UserViewSet, basename='customer')
router.register('Products', views.ProductViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
