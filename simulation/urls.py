from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CrewMemberViewSet, OxygenSystemViewSet, ShipStatusViewSet, sci_fi_dashboard

router = DefaultRouter()
router.register(r'crew', CrewMemberViewSet)
router.register(r'oxygen', OxygenSystemViewSet)
router.register(r'status', ShipStatusViewSet)

urlpatterns = router.urls + [
    path('dashboard/', sci_fi_dashboard, name='dashboard'),
]