from rest_framework import serializers

from profiles.models import Bio


class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = '__all__'
