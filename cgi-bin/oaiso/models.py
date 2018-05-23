from django.db import models
import uuid
from datetime import datetime
# Create your models here.

class Shop(models.Model):
    shop_name = models.TextField(null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    tel = models.TextField(null=True, blank=True)
    budget_lunch_min = models.TextField(null=True, blank=True)
    budget_lunch_max = models.TextField(null=True, blank=True)
    budget_dinner_min = models.TextField(null=True, blank=True)
    budget_dinner_max = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    lat = models.DecimalField(max_digits=16, decimal_places=13, null=True, blank=True)
    lng = models.DecimalField(max_digits=16, decimal_places=13, null=True, blank=True)


class Label_first (models.Model):
    budget_cheap = models.FloatField(null=True, blank=True)
    budget_reasonable = models.FloatField(null=True, blank=True)
    budget_expensive = models.FloatField(null=True, blank=True)
    priority_food = models.FloatField(null=True, blank=True)
    priority_drink = models.FloatField(null=True, blank=True)
    priority_atmosphere = models.FloatField(null=True, blank=True)
    priority_speed = models.FloatField(null=True, blank=True)
    can_alone = models.FloatField(null=True, blank=True)
    cannot_alone = models.FloatField(null=True, blank=True)


class Shop_info (models.Model):
    shop_name = models.TextField(null=True, blank=True)
    oaiso_genre = models.TextField(null=True, blank=True)
    super_genre = models.TextField(null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    tel = models.TextField(null=True, blank=True)
    bussiness_hours = models.TextField(null=True, blank=True)
    photo_food = models.TextField(null=True, blank=True)
    photo_shop = models.TextField(null=True, blank=True)
    budget_lunch_min = models.TextField(null=True, blank=True)
    budget_lunch_max = models.TextField(null=True, blank=True)
    budget_dinner_min = models.TextField(null=True, blank=True)
    budget_dinner_max = models.TextField(null=True, blank=True)
    links = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)


class Shop_label (models.Model):
    budget_cheap = models.FloatField(null=True, blank=True)
    budget_reasonable = models.FloatField(null=True, blank=True)
    budget_expensive = models.FloatField(null=True, blank=True)
    priority_food = models.FloatField(null=True, blank=True)
    priority_drink = models.FloatField(null=True, blank=True)
    priority_atmosphere = models.FloatField(null=True, blank=True)
    priority_speed = models.FloatField(null=True, blank=True)
    can_alone = models.FloatField(null=True, blank=True)
    cannot_alone = models.FloatField(null=True, blank=True)


