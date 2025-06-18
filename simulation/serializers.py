from rest_framework import serializers
from .models import CrewMember, OxygenSystem, ShipStatus

class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = '__all__'


class OxygenSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OxygenSystem
        fields = '__all__'


class ShipStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipStatus
        fields = '__all__'