#!/usr/bin/python
# coding: utf-8

import Shop
import pymysql.cursors

from csv_version.Vectorizor import Vectorizor


class Labeled_Shop(Shop.Shop):
  """docstring for Labeled_Shop"""
  def __init__(self, shop_info):
    self.id = shop_info['id']
    self.shop_name = shop_info['shop_name']
    self.regular_holiday = shop_info['regular_holiday']
    self.capacity_number = shop_info['capacity_number']
    self.card = shop_info['card']
    self.parking = shop_info['parking']
    self.private_room = shop_info['private_room']
    self.smoking = shop_info['smoking']
    self.free_drink_course = shop_info['free_drink_course']
    self.course = shop_info['course']
    self.location = shop_info['location']
    self.cuisine = shop_info['cuisine']
    self.reserved = shop_info['reserved']
    self.reservation_availability = shop_info['reservation_availability']
    self.transportation = shop_info['transportation']
    self.genre = shop_info['genre']
    self.facility = shop_info['facility']
    self.mobile_phone = shop_info['mobile_phone']
    self.scene = shop_info['scene']
    self.opening_date = shop_info['opening_date']
    self.budget_from_user_lunch_max = shop_info['budget_from_user_lunch_max']
    self.budget_from_user_night_max = shop_info['budget_from_user_night_max']
    self.budget_from_shop_lunch_max = shop_info['budget_from_shop_lunch_max']
    self.budget_from_shop_night_max = shop_info['budget_from_shop_night_max']

    self.priority_food = float(shop_info['priority_food'])
    self.priority_drink = float(shop_info['priority_drink'])
    self.priority_atmosphere = float(shop_info['priority_atmosphere'])
    self.priority_speed = float(shop_info['priority_speed'])
    self.can_alone = float(shop_info['can_alone'])
    self.cannot_alone = float(shop_info['cannot_alone'])

    self.genre_oaiso = shop_info['genre_oaiso']

    vectorizor = Vectorizor()
    self.vector = vectorizor.parseShop(self)
