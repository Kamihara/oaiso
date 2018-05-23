#!/usr/bin/python
# coding: utf-8


class Vectorizor():
    def __init__(self):
        pass

    def parseShop(self, labeled_shop):
        transportation = 0.5

        # regular_holiday
        if labeled_shop.regular_holiday.find('no data') < 0:
            regular_holiday = 0.9
        else:
            regular_holiday = 0.1

        # capacity_number
        try:
            capacity_number = (labeled_shop.capacity_number % 1000) / 1000.0
        except:
            capacity_number = 0.5

        # card
        if labeled_shop.card[0] == '不':
            card = 0.1
        elif labeled_shop.card[0] == '可':
            card = 0.9
        else:
            card = 0.5

        # parking
        if labeled_shop.parking[0] == '無':
            parking = 0.1
        elif labeled_shop.parking[0] == '有':
            parking = 0.9
        else:
            parking = 0.5

        # private_room
        if labeled_shop.private_room[0] == '無':
            private_room = 0.1
        elif labeled_shop.private_room[0] == '有':
            private_room = 0.9
        else:
            private_room = 0.5

        # smoking
        if labeled_shop.smoking.find('喫煙可') >= 0:
            smoking = 0.1
        elif labeled_shop.smoking.find('分煙') >= 0:
            smoking = 0.7
        elif labeled_shop.smoking.find('禁煙') >= 0:
            smoking = 0.8
        else:
            smoking = 0.5

        # free_drink_course
        if labeled_shop.free_drink_course == 'no data':
            free_drink_course = 0.1
        else:
            free_drink_course = 0.9

        # course
        if labeled_shop.course == 'no data':
            course = 0.1
        elif labeled_shop.course.find('食べ放題') >= 0:
            course = 0.5
        else:
            course = 0.9

        # location
        location = self.parseLocation(labeled_shop.location)

        # cuisine
        cuisine = self.parseCuisine(labeled_shop.cuisine)

        # reserved
        if labeled_shop.reserved[0] == '不':
            reserved = 0.1
        elif labeled_shop.reserved[0] == '可':
            reserved = 0.9
        else:
            reserved = 0.5

        # reservation_availability
        if labeled_shop.reservation_availability.find('予約可') == 0:
            reservation_availability = 0.1
        elif labeled_shop.reservation_availability.find('予約不可') == 0:
            reservation_availability = 0.9
        else:
            reservation_availability = 0.5

        # facility
        if labeled_shop.facility.find('カウンター席あり') >= 0:
            facility = 0.1
        elif labeled_shop.facility.find('オシャレな空間り') >= 0:
            facility = 0.3
        else:
            facility = 0.5

        # mobile_phone
        carriers = labeled_shop.mobile_phone.split('、')
        mobile_phone = len(carriers) / 10.0

        # scene
        scene = self.parseScene(labeled_shop.scene)

        # opening_date
        if labeled_shop.opening_date == 'no data':
            opening_date = 0.1
        else:
            opening_date = 0.9

        # budget_from_user_lunch_max
        try:
            val = float(labeled_shop.budget_from_user_lunch_max)
            budget_from_user_lunch_max = val / 30000.0
        except:
            budget_from_user_lunch_max = 0.0

        # budget_from_user_night_max
        try:
            val = float(labeled_shop.budget_from_user_night_max)
            budget_from_user_night_max = val / 30000.0
        except:
            budget_from_user_night_max = 0.0

        # budget_from_shop_lunch_max
        try:
            val = float(labeled_shop.budget_from_shop_lunch_max)
            budget_from_shop_lunch_max = val / 30000.0
        except:
            budget_from_shop_lunch_max = 0.0

        # budget_from_shop_night_max
        try:
            val = float(labeled_shop.budget_from_shop_night_max)
            budget_from_shop_night_max = val / 30000.0
        except:
            budget_from_shop_night_max = 0.0

        # genre
        genre = self.parseGenre(labeled_shop.genre_oaiso)

        point_list = [regular_holiday,
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
                budget_from_shop_night_max,
                ]

        points = []
        for p in point_list:
            if not isinstance(p, list):
                points.append(p)
                continue

            for pp in p:
                points.append(pp)

        return points

    def parseLocation(self, x):
        locations = [
            '隠れ家レストラン', '一軒家レストラン', '景色がきれい', '夜景が見える',
             'ホテルのレストラン', '海が見える', 'ホテルのレストラン'
        ]

        return []

        non_value = 0.5 if x == 'no data' else 0
        return [1 if l in x else non_value for l in locations]

    def parseCuisine(self, x):
        cuisines = [
            '魚料理にこだわる', '野菜料理にこだわる', '健康・美容メニューあり', 'ベジタリアンメニューあり'
        ]

        return []
        non_value = 0.5 if x == 'no data' else 0
        return [1 if c in x else non_value for c in cuisines]

    def parseScene(self, x):
        scenes = [
            '家族・子供と', '知人・友人と', '一人で入りやすい', '女子会', 'デート',
            '大人数の宴会', '合コン', '接待'
        ]

        scenes = [
            '家族・子供と', '知人・友人と', '一人で入りやすい'
        ]
        non_value = 0.5 if x == '' else 0
        return [1 if s in x else non_value for s in scenes]

    def parseGenre(self, x):
        genres = [
            'Ｂ級和食', '焼肉・ホルモン・鍋', '居酒屋', '高級和食', 'バー・お酒',
            '洋食・西洋料理', 'アジア・エスニック、中華料理'
        ]
        non_value = 0
        return [1 if g in x else non_value for g in genres]
