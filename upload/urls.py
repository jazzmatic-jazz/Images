from .views import PhotoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PhotoViewSet, basename='photo')
urlpatterns = router.urls