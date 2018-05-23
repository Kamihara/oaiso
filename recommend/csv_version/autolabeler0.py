#!/usr/bin/python # coding: utf-8
import csv

import numpy

from csv_version import Classifier
from csv_version.Labeled_Shop import Labeled_Shop


def get_labeled_shops():
    shops = []

    """
    select * from oaiso_label_first
      inner join tabelog.tabelog_shop_info on oaiso_label_first.id = tabelog.tabelog_shop_info.id;
    """
    with open('shop_info.csv') as label_file:
        reader = csv.reader(label_file)
        headers = []
        for row in reader:
            if len(headers) == 0:
                headers = row
                continue

            shop_info = {}
            for header, value in zip(headers, row):
                shop_info[header] = value
            shops.append(Labeled_Shop(shop_info))
    print(shops[0])
    return shops


def get_label(oclf, shop):
    label = oclf.predict(shop.vector)
    try:
        if shop.budget_from_user_night_max < 2000:
            label[0] = 3.0
        elif shop.budget_from_user_night_max < 5000:
            label[1] = 3.0
        else:
            label[2] = 3.0
    except:
        label[1] = 2.0
    return label


# clf
shops = get_labeled_shops()
oclf = Classifier.Classifier(shops[:100])

all_id = [shop.id for shop in shops]

food_diffs = []
for shop in shops:
    # 安い,中くらい,高価格,食べ,飲み,雰囲気,さくっと,一人で入れる,一人で入れない
    autolabel = get_label(oclf, shop)

    if shop.priority_food == 3:
        food_diffs.append(0 if autolabel[3] == 3 else 1)
    else:
        # food_diffs.append(1 if autolabel[3] == 3 else 0)
        if autolabel[3] == 3:
            food_diffs.append(0 if autolabel[3] > 1.5 else 1)
            print(
                "{}: 価格:{} 食:{} 飲:{} 雰囲気:{} さく:{} 一人で入れる:{} 一人で入れない".format(
                    shop.shop_name, [shop.budget_from_user_night_max, autolabel[0:3]],
                    [shop.priority_food, autolabel[3]], [shop.priority_drink, autolabel[4]],
                    [shop.priority_atmosphere, autolabel[5]], [shop.priority_speed, autolabel[6]],
                    [shop.can_alone, autolabel[7]], [shop.cannot_alone, autolabel[8]],
                ))

print(len(food_diffs), numpy.average(food_diffs), sum(food_diffs))
