from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    weather = models.CharField(max_length=100)
    irrigation_zone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.timestamp} - Temp: {self.temperature}°C"
