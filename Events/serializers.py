from rest_framework import serializers
from .models import Event, RegisterEvent


class EventSerializer(serializers.ModelSerializer):
    description = serializers.CharField(write_only=True)
    image = serializers.ImageField(write_only=True)
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'text',
            'location',
            'description',
            'date',
            'start_time',
            'end_time',
            'image',
        )


class RegisterEventSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = RegisterEvent
        fields = (
            'full_name',
            'email',
            'phone',
            'status',
        )




class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'text',
            'location',
            'description',
            'date',
            'start_time',
            'end_time',
            'image',
            'highlight_1',
            'highlight_2',
            'highlight_3',
            'highlight_4',
            'highlight_5',
            'image_1',
            'image_2',
            'image_3',
        )
