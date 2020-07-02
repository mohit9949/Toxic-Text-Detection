from rest_framework import serializers
from .models import apiqueryDB

class apiSerializers(serializers.ModelSerializer):
    class Meta:
        model=apiqueryDB
        fields='__all__'
