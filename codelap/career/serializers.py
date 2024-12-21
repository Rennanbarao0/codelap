from rest_framework import serializers

from .models import Careers

class CareersSerializers(serializers.ModelSerializer): 
    class Meta: 
        model = Careers
        fields = '__all__'
