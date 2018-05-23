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
      print('err0')
      sys.exit()
    conn.close()

  shops = []
  for row in ret:
    shop = ls.Labeled_Shop(row['id'])
    if shop.id:
      shops.append(shop)

  return shops

def get_label(oclf, shop_id):
  shop = Shop(shop_id)
  try:
    if not shop:
      return None
    if not shop.vector:
      return None
  except:
    return None
  label = oclf.predict(shop.vector)
  try:
    if shop.budget_from_user_night_max < 3000:
      label[0] = 3.0
    elif shop.budget_from_user_night_max < 6000:
      label[1] = 3.0
    else:
      label[2] = 3.0
  except:
    label[1] = 2.0
  return label

# clf
shops = get_labeled_shops()
oclf = Classifier.Classifier(shops)

# all
conn = pymysql.connect(
  user = 'root',
  password = 'nakano02',
  host = 'localhost',
  db = 'oaiso',
  charset = 'utf8',
  cursorclass = pymysql.cursors.DictCursor)

all_id = []
with conn.cursor() as cur:
  #sql = 'select distinct id from tabelog_shop_info;'
#  sql = '''
#select id
#  from oaiso.oaiso_shop_info
#    where id not in
#      (select id from oaiso.oaiso_shop_label);
#'''
  sql = 'select id from oaiso_shop_info;'
  cur.execute(sql)
  ret = cur.fetchall()
  if not ret:
    print('err1')
    sys.exit()
  conn.close()
  for row in ret:
    all_id.append(row['id'])

# dist
conn = pymysql.connect(
  user = 'root',
  password = 'nakano02',
  host = 'localhost',
  db = 'oaiso',
  charset = 'utf8',
  cursorclass = pymysql.cursors.DictCursor)

for i,id in enumerate(all_id):
  # if i>10:
  #   break
  print('\r{0}/{1}'.format(i+1, len(all_id)), end='')
  autolabel = get_label(oclf, id)
  if not autolabel:
    continue
  sql = '''
update oaiso_shop_label set
  budget_cheap={},
  budget_reasonable={},
  budget_expensive={},
  priority_food={},
  priority_drink={},
  priority_atmosphere={},
  priority_speed={},
  can_alone={},
  cannot_alone={}
where id={};
'''.format(*autolabel, id)
  with conn.cursor() as cur:
    cur.execute(sql)
    conn.commit()
    if not cur.rowcount:
      sql = '''insert into oaiso_shop_label(
      budget_cheap,
      budget_reasonable,
      budget_expensive,
      priority_food,
      priority_drink,
      priority_atmosphere,
      priority_speed,
      can_alone,
      cannot_alone
      ) values({},{},{},{},{},{},{},{},{});
    '''.format(*autolabel)
    cur.execute(sql)
    conn.commit()
conn.close()
