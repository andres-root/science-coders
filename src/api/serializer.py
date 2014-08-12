from django.forms import widgets
from rest_framework import serializers
from web.models import Science


class ScienceSerializer(serializer.ModelSerializers):
    class Meta:
        model = Science
        fields = ('id', 'name', 'code', 'description', 'active', 'deleted', 'date_created', 'date_updated')
