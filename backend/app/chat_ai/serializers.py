from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import *
from .tale_ai_function import sent_prompt_and_get_response


class TalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tales
        fields = '__all__'

    def create(self, validated_data):
        text = validated_data.get('text')

        # Генерация текста сказки
        if text:
            generated_story = sent_prompt_and_get_response(text)
            validated_data['text'] = generated_story

        # Получаем пользователя из контекста
        user = self.context['request'].user

        # Проверка, что пользователь аутентифицирован
        if user.is_anonymous:
            raise ValidationError("Пожалуйста, авторизуйтесь, чтобы создать сказку.")

        # Присваиваем пользователя в validated_data
        validated_data['user'] = user

        # Создаем объект модели
        return super().create(validated_data)


class TopTalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopTales
        fields = '__all__'
