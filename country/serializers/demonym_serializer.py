from rest_framework import serializers
from country.models import Demonym


class DemonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demonym
        fields = "__all__"
