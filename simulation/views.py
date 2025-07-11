from django.shortcuts import render
from rest_framework import viewsets
from .models import CrewMember, OxygenSystem, ShipStatus
from .serializers import CrewMemberSerializer, OxygenSystemSerializer, ShipStatusSerializer

class CrewMemberViewSet(viewsets.ModelViewSet):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer


class OxygenSystemViewSet(viewsets.ModelViewSet):
    queryset = OxygenSystem.objects.all()
    serializer_class = OxygenSystemSerializer


class ShipStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShipStatus.objects.all().order_by('-timestamp')[:10]
    serializer_class = ShipStatusSerializer


def sci_fi_dashboard(request):
    context = {
        "crew_list": CrewMember.objects.all(),
        "oxygen_list": OxygenSystem.objects.all(),
        "status_list": ShipStatus.objects.order_by("-timestamp")[:10]
    }

    return render(request, "dashboard.html", context)