from django.contrib.auth.models import User, Group
from rest_framework import serializers

from oaiso.models import Shop, Shop_info


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'shop_name', 'review', 'tel', 'address', 'photo', 'lat', 'lng', 'budget_dinner_min', 'budget_dinner_max', 'budget_lunch_min', 'budget_lunch_max']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop_info
        fields = ['id', 'shop_name', 'genre', 'review', 'bussiness_hours', 'links', 'photo_shop', 'photo_food', 'budget_dinner_min', 'budget_dinner_max', 'budget_lunch_min', 'budget_lunch_max', 'tel', 'address', 'lat', 'lng']

        

