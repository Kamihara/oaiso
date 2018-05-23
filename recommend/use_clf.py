#!/usr/bin/python
# coding: utf-8

import sys
import pymysql.cursors
import Classifier
import Labeled_Shop as ls
from Shop import Shop

def get_labeled_shops():
  conn = pymysql.connect(
    user = 'root',
    password = 'nakano02',
    host = 'localhost',
    db = 'oaiso',
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor)

  with conn.cursor() as cur:
    sql = 'select id from oaiso_label_first;'
    cur.execute(sql)
    ret = cur.fetchall()
    if not ret:
      sys.exit()
    conn.close()

  shops = []
  for row in ret:
    shop = ls.Labeled_Shop(row['id'])
    if shop.id:
      shops.append(shop)
  return shops

#def get_label(shop_id):
#  shops = get_labeled_shops()
#  oclf = Classifier.Classifier(shops)
#  shop = Shop(shop_id)
#  label = oclf.predict(shop.vector)
#  try:
#    if shop.budget_from_user_night_max < 2000:
#      label[0] = 3.0
#    elif shop.budget_from_user_night_max < 5000:
#      label[1] = 3.0
#    else:
#      label[2] = 3.0
#  except:
#    label[1] = 2.0
#  return label

# clf
shops = get_labeled_shops()
oclf = Classifier.Classifier(shops)


oclf.scores()


