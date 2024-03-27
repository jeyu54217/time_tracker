from rest_framework import serializers
from django.db.models import Q
from .models import (Date, Time, Act_type, Act_name)


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'
        lookup_field = 'id' 

class TimeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Time
        fields = ['date', 'start_time', 'end_time', 'act_type', 'act_name', 'notes']
        lookup_field = 'id'

class ActTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Act_type
        fields = '__all__'
        lookup_field = 'id'

class ActNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Act_name
        fields = '__all__'
        lookup_field = 'id' 



class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['user', 'date']

    def create(self, validated_data):
        date, created = Date.objects.update_or_create(
            Q(user = validated_data['user']) & 
            Q(date = validated_data['date']), 
            defaults = validated_data
        ) # returns a tuple of two elements: object & boolean indicating whether the object was created or not.
        return date

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['date', 'start_time', 'end_time', 'act_type', 'act_name', 'notes']

    def create(self, validated_data):
        time, created = Time.objects.update_or_create(
            Q(date = validated_data['date']) & 
            Q(start_time = validated_data['start_time']) & 
            Q(end_time = validated_data['end_time']), 
            defaults = validated_data
        )
        return time