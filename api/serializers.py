from rest_framework import serializers
from apptodo.models import todotask

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todotask
        fields = "__all__"