from rest_framework.routers import DefaultRouter
from .views import CrewMemberViewSet, OxygenSystemViewSet, ShipStatusViewSet

router = DefaultRouter()
router.register(r'crew', CrewMemberViewSet)
router.register(r'oxygen', OxygenSystemViewSet)
router.register(r'status', ShipStatusViewSet)

urlpatterns = router.urls