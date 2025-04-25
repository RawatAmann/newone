from django.shortcuts import render
from .models import SensorData
import pyrebase
from datetime import datetime

firebase_config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_PROJECT.firebaseapp.com",
    "databaseURL": "https://YOUR_PROJECT.firebaseio.com",
    "storageBucket": "YOUR_PROJECT.appspot.com",
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

def dashboard_view(request):
    # Get real-time data from Firebase
    data = db.child("sensor_data").get().val()
    
    # Save to database (if new)
    if data:
        timestamp = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S')
        if not SensorData.objects.filter(timestamp=timestamp).exists():
            SensorData.objects.create(
                timestamp=timestamp,
                temperature=data['temperature'],
                humidity=data['humidity'],
                soil_moisture=data['soil_moisture'],
                weather=data['weather'],
                irrigation_zone=data['irrigation_zone']
            )
    
    return render(request, 'dashboard.html', {'data': data})
