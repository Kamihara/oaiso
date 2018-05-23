#!/usr/bin/python
# coding: utf-8

import pymysql.cursors

class Vectorizor():
  def __init__(self):
    pass
  
  def parseShop(self, shop):

    # stab
    transportation = 0.5

    # regular_holiday
    if shop.regular_holiday.find('no data') < 0:
      regular_holiday = 0.9
    else:
      regular_holiday = 0.1

    # capacity_number
    try:
      capacity_number  = (shop.capacity_number % 1000) / 1000.0
    except:
      capacity_number = 0.5

    # card
    if shop.card[0] == '不':
      card = 0.1
    elif shop.card[0] == '可':
      card = 0.9
    else:
      card = 0.5

    # parking
    if shop.parking[0] == '無':
      parking = 0.1
    elif shop.parking[0] == '有':
      parking = 0.9
    else:
      parking = 0.5

    # private_room
    if shop.private_room[0] == '無':
      private_room = 0.1
    elif shop.private_room[0] == '有':
      private_room = 0.9
    else:
      private_room = 0.5

    # smoking
    if shop.smoking.find('喫煙可') >= 0:
      smoking = 0.1
    elif shop.smoking.find('分煙') >= 0:
      smoking = 0.7
    elif shop.smoking.find('禁煙') >= 0:
      smoking = 0.8
    else:
      smoking = 0.5

    # free_drink_course
    if shop.free_drink_course == 'no data':
      free_drink_course = 0.1
    else:
      free_drink_course = 0.9

    # course
    if shop.course == 'no data':
      course = 0.1
    elif shop.course.find('食べ放題') >= 0:
      course = 0.5
    else:
      course = 0.9

    # location
    location = self.parseLocation(shop.location)

    # cuisine
    cuisine = self.parseCuisine(shop.cuisine)

    # reserved
    if shop.reserved[0] == '不':
      reserved = 0.1
    elif shop.reserved[0] == '可':
      reserved = 0.9
    else:
      reserved = 0.5

    # reservation_availability
    if shop.reservation_availability.find('予約可') == 0:
      reservation_availability = 0.1
    elif shop.reservation_availability.find('予約不可') == 0:
      reservation_availability = 0.9
    else:
      reservation_availability = 0.5

    # facility
    if shop.facility.find('カウンター席あり') >= 0:
      facility = 0.1
    elif shop.facility.find('オシャレな空間り') >= 0:
      facility = 0.3
    else:
      facility = 0.5

    # mobile_phone
    carriers = shop.mobile_phone.split('、')
    mobile_phone = len(carriers) / 10.0

    # scene
    scene = self.parseScene(shop.scene)

    # opening_date
    if shop.opening_date == 'no data':
      opening_date = 0.1
    else:
      opening_date = 0.9

    # budget_from_user_lunch_max
    try:
      val = float(shop.budget_from_user_lunch_max)
      budget_from_user_lunch_max = val / 30000.0
    except:
      budget_from_user_lunch_max = 0.0

    # budget_from_user_night_max
    try:
      val = float(shop.budget_from_user_night_max)
      budget_from_user_night_max = val / 30000.0
    except:
      budget_from_user_night_max = 0.0

    # budget_from_shop_lunch_max
    try:
      val = float(shop.budget_from_shop_lunch_max)
      budget_from_shop_lunch_max = val / 30000.0
    except:
      budget_from_shop_lunch_max = 0.0

    # budget_from_shop_night_max
    try:
      val = float(shop.budget_from_shop_night_max)
      budget_from_shop_night_max = val / 30000.0
    except:
      budget_from_shop_night_max = 0.0

    # genre
    genre = 0.0
    dbname = 'oaiso'
    conn = pymysql.connect(user='root', password='nakano02', host='localhost',
      db=dbname, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    with conn.cursor() as cur:
      sql = '''select distinct oaiso_genre from oaiso_shop_info
        where id={0}'''.format(shop.id)
      cur.execute(sql)
      ret = cur.fetchall()
      if ret:
        genre = self.parseGenre(ret[0]['oaiso_genre'])
    
    # images_count
    #dish_drink_ratio = shop.dish_images_count / shop.drink_images_count

    return (regular_holiday,
    capacity_number,
    card,
    parking,
    private_room,
    smoking,
    free_drink_course,
    course,
    location,
    cuisine,
    reserved,
    reservation_availability,
    transportation,
    genre,
    facility,
    mobile_phone,
    scene,
    opening_date,
    budget_from_user_lunch_max,
    budget_from_user_night_max,
    budget_from_shop_lunch_max,
    budget_from_shop_night_max
    )
    #dish_drink_ratio)





  def parseLocation(self, x):
    dic = {
  'no data': 0.02,
  '隠れ家レストラン': 0.0555,
  '隠れ家レストラン、一軒家レストラン': 0.091,
  '一軒家レストラン': 0.1265,
  '景色がきれい、隠れ家レストラン': 0.162,
  '夜景が見える': 0.1975,
  'ホテルのレストラン': 0.233,
  '景色がきれい、一軒家レストラン': 0.2685,
  '景色がきれい、夜景が見える': 0.304,
  '夜景が見える、隠れ家レストラン': 0.3395,
  '景色がきれい、夜景が見える、海が見える': 0.375,
  '景色がきれい、隠れ家レストラン、一軒家レストラン': 0.4105,
  '景色がきれい': 0.446,
  '夜景が見える、隠れ家レストラン、一軒家レストラン': 0.4815,
  '景色がきれい、夜景が見える、隠れ家レストラン': 0.517,
  '景色がきれい、夜景が見える、隠れ家レストラン、一軒家レストラン': 0.5525,
  '景色がきれい、ホテルのレストラン': 0.588,
  '景色がきれい、夜景が見える、ホテルのレストラン': 0.6235,
  '景色がきれい、夜景が見える、一軒家レストラン': 0.659,
  '景色がきれい、夜景が見える、海が見える、ホテルのレストラン': 0.6945,
  '景色がきれい、夜景が見える、ホテルのレストラン、隠れ家レストラン': 0.73,
  '景色がきれい、夜景が見える、海が見える、ホテルのレストラン、隠れ家レストラン': 0.7655,
  '夜景が見える、ホテルのレストラン': 0.801,
  '景色がきれい、夜景が見える、海が見える、ホテルのレストラン、隠れ家レストラン、一軒家レストラン': 0.8365,
  'ホテルのレストラン、隠れ家レストラン': 0.872,
  '景色がきれい、夜景が見える、ホテルのレストラン、隠れ家レストラン、一軒家レストラン': 0.9075
    }
    try:
      return dic[x]
    except:
      return 0.0

  def parseCuisine(self, x):
    dic = {
  'no data': 0.02,
  '魚料理にこだわる': 0.08,
  '野菜料理にこだわる、健康・美容メニューあり': 0.14,
  '野菜料理にこだわる、魚料理にこだわる': 0.2,
  '野菜料理にこだわる、魚料理にこだわる、健康・美容メニューあり、ベジタリアンメニューあり': 0.26,
  'ベジタリアンメニューあり': 0.32,
  '野菜料理にこだわる': 0.38,
  '野菜料理にこだわる、ベジタリアンメニューあり': 0.44,
  '野菜料理にこだわる、魚料理にこだわる、健康・美容メニューあり': 0.5,
  '魚料理にこだわる、健康・美容メニューあり': 0.56,
  '健康・美容メニューあり': 0.62,
  '野菜料理にこだわる、健康・美容メニューあり、ベジタリアンメニューあり': 0.68,
  '健康・美容メニューあり、ベジタリアンメニューあり': 0.74,
  '野菜料理にこだわる、魚料理にこだわる、ベジタリアンメニューあり': 0.8,
  '魚料理にこだわる、ベジタリアンメニューあり': 0.86,
  '魚料理にこだわる、健康・美容メニューあり、ベジタリアンメニューあり': 0.92
    }
    try:
      return dic[x]
    except:
      return 0.0

  def parseScene(self, x):
    dic = {
  '空欄のとき': 0.02,
  '家族・子供と｜知人・友人と': 0.044,
  '家族・子供と': 0.068,
  '知人・友人と': 0.092,
  '家族・子供と｜一人で入りやすい｜知人・友人と': 0.116,
  '一人で入りやすい｜知人・友人と': 0.14,
  '家族・子供と｜女子会｜一人で入りやすい｜知人・友人と': 0.164,
  '一人で入りやすい': 0.188,
  '家族・子供と｜デート｜知人・友人と': 0.212,
  '家族・子供と｜一人で入りやすい': 0.236,
  '家族・子供と｜女子会｜知人・友人と': 0.26,
  'デート｜知人・友人と': 0.284,
  '女子会｜大人数の宴会｜知人・友人と': 0.308,
  '女子会｜知人・友人と': 0.332,
  '大人数の宴会｜知人・友人と': 0.356,
  '女子会｜一人で入りやすい': 0.38,
  '家族・子供と｜デート': 0.404,
  'デート｜一人で入りやすい｜知人・友人と': 0.428,
  '女子会｜一人で入りやすい｜知人・友人と': 0.452,
  '家族・子供と｜接待｜知人・友人と': 0.476,
  '家族・子供と｜女子会': 0.5,
  '女子会': 0.524,
  '家族・子供と｜女子会｜合コン': 0.548,
  'デート': 0.572,
  '家族・子供と｜デート｜一人で入りやすい｜知人・友人と': 0.596,
  '接待｜知人・友人と': 0.62,
  '家族・子供と｜接待': 0.644,
  '家族・子供と｜女子会｜一人で入りやすい': 0.668,
  '家族・子供と｜デート｜一人で入りやすい': 0.692,
  '家族・子供と｜合コン｜大人数の宴会｜知人・友人と': 0.716,
  '家族・子供と｜女子会｜大人数の宴会｜知人・友人と': 0.74,
  'デート｜接待｜知人・友人と': 0.764,
  'デート｜接待': 0.788,
  '接待': 0.812,
  '家族・子供と｜デート｜接待｜知人・友人と': 0.836,
  '家族・子供と｜デート｜接待': 0.86,
  'デート｜一人で入りやすい': 0.884,
  '女子会｜合コン｜知人・友人と': 0.908,
  '女子会｜大人数の宴会｜一人で入りやすい｜知人・友人と': 0.932
    }
    try:
      return dic[x]
    except:
      return 0.0

  def parseGenre(self, x):
    dic = {
    'Ｂ級和食': 0.02,
    '焼肉・ホルモン・鍋': 0.14,
    '居酒屋': 0.26,
    '高級和食': 0.38,
    'バー・お酒': 0.5,
    '洋食・西洋料理': 0.62,
    'アジア・エスニック、中華料理': 0.74,
    'NULL': 0.86
    }
    try:
      return dic[x]
    except:
      return 0.0
