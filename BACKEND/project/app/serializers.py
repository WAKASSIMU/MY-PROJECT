from rest_framework import serializers
from .models import *

class ChairpersonSesrializer(serializers.ModelSerializer):
    class Meta:
        model= Chairperson
        fields = '__all__'