from django.db import models

class CrewMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    oxygen_consumption = models.FloatField(default=0.5)

    def __str__(self):
        return f"{self.name} - {self.role}"


class OxygenSystem(models.Model):
    level = models.FloatField(default=100.0)
    prodution_rate = models.FloatField(default=2.0)
    status = models.CharField(max_length=50, default="Online")

    def __str__(self):
        return f"Oxigen: {self.level}% [{self.status}]"


class ShipStatus(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    oxygen_level = models.FloatField()
    crew_count = models.IntegerField()
    alert = models.TextField(blank=True)