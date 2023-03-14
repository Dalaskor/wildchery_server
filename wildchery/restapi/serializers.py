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
    # category = serializers.StringRelatedField(read_only=True)
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset = Category.objects
    )

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category'] 
        # fields = '__all__' 


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    sub_category = serializers.StringRelatedField(source='sub_category.name')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'sub_category']

