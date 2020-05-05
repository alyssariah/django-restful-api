from rest_framework import serializers
from apps.api.models import FoodLog

class FoodLogSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FoodLog
        fields = ('id', 'date', 'name_of_food', 'owner',  'day_of_the_week', 'meal', 'description', 'calories', 'updated_at', 'is_public',)