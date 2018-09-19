from rest_framework import serializers
from .models import MasterPlanHouse

class ActivityDateSerializer(serializers.ModelSerializer):
    """
    This serialzer is to show activity start date and end date
    """
    class Meta:
        model = MasterPlanHouse
        fields = (
            'activity','start_date','end_date')
