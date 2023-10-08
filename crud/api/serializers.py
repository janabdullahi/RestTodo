from rest_framework import serializers
from .models import Crud

class CrudSerializers(serializers.ModelSerializer):
    class Meta:
        model = Crud
        fields = '__all__'