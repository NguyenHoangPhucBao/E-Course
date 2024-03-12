from rest_framework.serializers import ModelSerializer
from .models import Course, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'active', 'category']