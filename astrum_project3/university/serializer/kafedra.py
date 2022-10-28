from Django_REST.astrum_project3.university.models.kafedra import Kafedra
from rest_framework import serializers


class KafedraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kafedra
        fields = '__all__'
