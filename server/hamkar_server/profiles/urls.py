
from rest_framework.routers import DefaultRouter
from .views import  UserInformationViewSet

router = DefaultRouter()
router.register(r'user-info', UserInformationViewSet)

urlpatterns = router.urls
