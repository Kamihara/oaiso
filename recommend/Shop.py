#!/usr/bin/python
# coding: utf-8

import pymysql.cursors
import Vectorizor as vec

class Shop():
  """docstring for Shop"""
  def __init__(self, id):
    self.id = id

    # todo xxx ???
    # need check if id is both in label_first
    # shop_test

    # db and 
    conn = pymysql.connect(
      user = 'root', 
      password = 'nakano02', 
      host = 'localhost', 
      db = 'shop_analysis', 
      charset = 'utf8', 
      cursorclass = pymysql.cursors.DictCursor)
    with conn.cursor() as cur:
      sql = 'select * from tabelog_shop_info where id={0};'.format(self.id)
      cur.execute(sql)
      ret = cur.fetchall()
      conn.close()

    # if no info in db
    if not ret:
      self.id = 0
      return None

    # gives err if columns are not perfect
    try:
      row = ret[0]
      self.shop_name = row['shop_name']
      self.regular_holiday = row['regular_holiday']
      self.capacity_number = row['capacity_number']
      self.card = row['card']
      self.parking = row['parking']
      self.private_room = row['private_room']
      self.smoking = row['smoking']
      self.free_drink_course = row['free_drink_course']
      self.course = row['course']
      self.location = row['location']
      self.cuisine = row['cuisine']
      self.reserved = row['reserved']
      self.reservation_availability = row['reservation_availability']
      self.transportation = row['transportation']
      self.genre = row['genre']
      self.facility = row['facility']
      self.mobile_phone = row['mobile_phone']
      self.scene = row['scene']
      self.opening_date = row['opening_date']
      self.budget_from_user_lunch_max = row['budget_from_user_lunch_max']
      self.budget_from_user_night_max = row['budget_from_user_night_max']
      self.budget_from_shop_lunch_max = row['budget_from_shop_lunch_max']
      self.budget_from_shop_night_max = row['budget_from_shop_night_max']
      self.dish_images_count = row['dish_images_count']
      self.drink_images_count = row['drink_images_count']
      
      vectorizor = vec.Vectorizor()
      self.vector = vectorizor.parseShop(self)
    except:
      pass
