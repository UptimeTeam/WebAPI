from rest_framework import serializers
from postss.models import Post
from django.forms import SelectDateWidget
from django.utils import timezone


class TimePickerWidget(serializers.CharField):
    input_type = 'time'


class PostSerializer(serializers.ModelSerializer):
    training_date = serializers.DateField(
        format='%Y-%m-%d', input_formats=['%Y-%m-%d'])

    training_time = serializers.TimeField(
        label='Время', widget=TimePickerWidget(), initial=timezone.now().time())

    class Meta:
        model = Post
        fields = ['title', 'court', 'training_date',
                  'training_time', 'preferences']
