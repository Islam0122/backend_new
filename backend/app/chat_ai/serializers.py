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
        text = validated_data.get('text')
        generated_story = sent_prompt_and_get_response(text)
        validated_data['text'] = generated_story

        user = self.context['request'].user

        # Для анонимных пользователей сохраняем сказку без привязки к пользователю
        if user.is_anonymous:
            validated_data['user'] = None
        else:
            validated_data['user'] = user

        # Создаем объект модели
        return super().create(validated_data)


class TopTalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopTales
        fields = '__all__'
