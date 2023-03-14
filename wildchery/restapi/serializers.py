from rest_framework import serializers
from .models import *


class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = userProfile
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset = Category.objects
    )

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category'] 


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    sub_category = serializers.SlugRelatedField(
        slug_field='name',
        queryset = SubCategory.objects
    )

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'sub_category']


class ProductPhotoSerializer(serializers.HyperlinkedModelSerializer):
    sub_category = serializers.SlugRelatedField(
        slug_field='id',
        queryset = Product.objects
    )

    class Meta:
        model = ProductPhoto
        fields = ['image', 'product']

