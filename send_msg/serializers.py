from rest_framework import serializers

from .models import WXGROUP


class WXGROUPSerializer(serializers.ModelSerializer):

    class Meta:
        model = WXGROUP
        fields = '__all__'

