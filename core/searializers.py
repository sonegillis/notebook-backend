from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        exclude = ['user']

    def create(self, validated_data):
        return Note.objects.create(user=self.context['request'].user, **validated_data)

