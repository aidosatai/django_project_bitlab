from rest_framework import serializers

from main.models import Category
class CategoryAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    publish_date= serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Category
        fields = 'id', 'category_name', 'publish_date'


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'category_name', 'publish_date'




