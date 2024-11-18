from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import *
from .tale_ai_function import sent_prompt_and_get_response


class TalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tales
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False, 'allow_null': True}  # Поле необязательно
        }

    def create(self, validated_data):
        try:
            text = validated_data.get('text')
            generated_story = sent_prompt_and_get_response(text)
            validated_data['text'] = generated_story

            user = self.context['request'].user
            validated_data['user'] = user if not user.is_anonymous else None

            return super().create(validated_data)
        except Exception as e:
            raise serializers.ValidationError({"detail": f"Ошибка при создании сказки: {str(e)}"})


class TopTalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopTales
        fields = '__all__'
