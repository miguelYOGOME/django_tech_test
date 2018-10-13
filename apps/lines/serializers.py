from rest_framework import serializers
from .models import LineModel, RouteModel

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineModel
        fields = ('id', 'name', 'color')
    
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        fields = ('id', 'line', 'stations', 'direction', 'is_active')