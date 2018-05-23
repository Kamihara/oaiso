#!/usr/bin/python
# coding: utf-8

import Shop
import pymysql.cursors

class Labeled_Shop(Shop.Shop):
  """docstring for Labeled_Shop"""
  def __init__(self, id):
    super(Labeled_Shop, self).__init__(id)
    # self.arg = arg

    conn = pymysql.connect(
      user = 'root',
      password = 'nakano02',
      host = 'localhost',
      db = 'oaiso',
      charset = 'utf8',
      cursorclass = pymysql.cursors.DictCursor)
    with conn.cursor() as cur:
      sql = '''select * from oaiso_label_first
        where id={0};'''.format(self.id)
      cur.execute(sql)
      ret = cur.fetchall()
      conn.close()

    if not ret:
      self.id = 0
      return None

    row = ret[0]
    self.priority_food = row['priority_food']
    self.priority_drink = row['priority_drink']
    self.priority_atmosphere = row['priority_atmosphere']
    self.priority_speed = row['priority_speed']
    self.can_alone = row['can_alone']
    self.cannot_alone = row['cannot_alone']