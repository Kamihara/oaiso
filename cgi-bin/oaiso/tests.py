from django.test import TestCase
from oaiso.models import Shop_info, Label_first, Shop_label
from django.db.models import Q
import math
import pyproj
import numpy as np


# Create your tests here.
# 何らかの計算結果の降順(大きい順)に飲食店のidを返す関数
def return_id(score_list):
	score_list_sort = sorted(score_list, key=lambda x:x[1], reverse=True)
	sim_array = np.array(score_list_sort)
	id_list = list(map(int, list(sim_array[:, 0])))
	return id_list

# 何らかの計算結果の昇順に飲食店のidとを返す関数
def return_id_up(dlist):
	dlist_sort = sorted(dlist, key=lambda x:x[1])
	darray = np.array(dlist_sort)
	id_list = list(map(int, list(darray[:, 0])))
	return id_list

#距離の昇順に飲食店のidと距離を返す関数
def distsort(dlist):
	dlist_sort = sorted(dlist, key=lambda x:x[1])
	return dlist_sort

#コサイン類似度
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# 距離を計算して店のidと一緒に返す関数
def return_distance(ulat, ulng):
	grs80 = pyproj.Geod(ellps='GRS80')
	distance_list = []

	for row in Shop_info.objects.values_list('id', 'lat', 'lng').order_by('id'):
		shop_id = row[0]
		lat = row[1]
		lng = row[2]

		if lat is None or lng is None:
			pass

		else:
			g = grs80.inv(lng, lat, ulng, ulat)
			distance_list.append([shop_id, g[2]])

	return distance_list


# 距離フィルタリング関数
"""
def distance_filter(dist_reference, req_lat, req_lng):
	dist_list = []
	distance_list = return_distance(req_lat, req_lng) #店のidと現在地からの距離のリスト
	#dist_reference = 0

	for row in distance_list:
		if row[1] <= dist_reference:	
			dist_list.append([row[0], row[1]])

	return (dist_reference, dist_list)
"""

def distance_filter(num, req_lat, req_lng):
	dist_list = []
	distance_list = return_distance(req_lat, req_lng) #店のidと現在地からの距離のリスト
	dist_reference = 0

	while True:
		dist_reference += 1
		for row in distance_list:
			if row[1] <= dist_reference:	
				dist_list.append([row[0], row[1]])
				continue
		
		dist_list = list(map(list, set(map(tuple, dist_list))))
		if len(dist_list) >= num:
			return (dist_reference, dist_list)
			break


# 内容ベースフィルタリング関数
def contents_filter(dist_ref, dlist, uvec):
	score_list = []	#oaisoスコアのリスト初期化
	user_vec = np.array(uvec)	#ユーザベクトル(user_vec)をNumPy配列で受け取り
	uvec_str = ','.join([str(i) for i in uvec])
	d_sorted = sorted(dlist, key=lambda x:x[0]) #dlistをid順に並び替え

	#飲食店のラベリングデータの呼び出し
	if user_vec[0] != 0: #価格帯が低いとき
		for row in d_sorted:
			shop_id = row[0] #店のid
			shop_dist = row[1] #店の距離

			for label in Label_first.objects.all().filter(id=shop_id).filter(~Q(budget_cheap = 0)).values_list():
				list_label = list(label)

				shop_vec = np.array(list_label[4:9])	#飲食店の特徴ベクトル(NumPy配列)
				svec_str = ','.join([str(i) for i in (list_label[1:])]) #特徴ベクトル文字列
				shop_name = Shop_info.objects.all().filter(id=shop_id).values_list('shop_name', flat=True) #shop_name
				links = Shop_info.objects.all().filter(id=shop_id).values_list('links', flat=True) #links
				genre = Shop_info.objects.all().filter(id=shop_id).values_list('genre', flat=True) #genre
				oaiso_genre = Shop_info.objects.all().filter(id=shop_id).values_list('oaiso_genre', flat=True) #oaiso_genre
				lat = Shop_info.objects.all().filter(id=shop_id).values_list('lat', flat=True) #lat
				lng = Shop_info.objects.all().filter(id=shop_id).values_list('lng', flat=True) #lng
				address = Shop_info.objects.all().filter(id=shop_id).values_list('address', flat=True) #address
				budget_lunch_min = Shop_info.objects.all().filter(id=shop_id).values_list('budget_lunch_min', flat=True)
				budget_lunch_max = Shop_info.objects.all().filter(id=shop_id).values_list('budget_lunch_max', flat=True)
				budget_dinner_min = Shop_info.objects.all().filter(id=shop_id).values_list('budget_dinner_min', flat=True)
				budget_dinner_max = Shop_info.objects.all().filter(id=shop_id).values_list('budget_dinner_max', flat=True)

				sim_score = cos_sim(user_vec[3:8], shop_vec) #cos類似度のスコア
				dist_score = (dist_ref - shop_dist)/dist_ref #距離スコア
				oaiso_score = math.sqrt(sim_score*sim_score + dist_score*dist_score) #総合スコア

				score_list.append(
					[uvec_str, 
					svec_str, 
					dist_score, 
					shop_dist,
					sim_score, 
					oaiso_score, 
					str(shop_id), 
					list(shop_name)[0], 
					list(links)[0],
					list(genre)[0],
					list(oaiso_genre)[0],
					list(lat)[0],
					list(lng)[0],
					list(address)[0],
					list(budget_lunch_min)[0],
					list(budget_lunch_max)[0],
					list(budget_dinner_min)[0],
					list(budget_dinner_max)[0]]
					)
		
		score_list = list(map(list, set(map(tuple, score_list))))		
		return sorted(score_list, key=lambda x:x[5], reverse=True)  #oaiso_score順に並び替える


	elif user_vec[1] != 0: #価格帯が低いとき
		for row in d_sorted:
			shop_id = row[0] #店のid
			shop_dist = row[1] #店の距離

			for label in Label_first.objects.all().filter(id=shop_id).filter(~Q(budget_reasonable = 0)).values_list():
				list_label = list(label)

				shop_vec = np.array(list_label[4:9])	#飲食店の特徴ベクトル(NumPy配列)
				svec_str = ','.join([str(i) for i in (list_label[1:])]) #特徴ベクトル文字列
				shop_name = Shop_info.objects.all().filter(id=shop_id).values_list('shop_name', flat=True) #shop_name
				links = Shop_info.objects.all().filter(id=shop_id).values_list('links', flat=True) #links
				genre = Shop_info.objects.all().filter(id=shop_id).values_list('genre', flat=True) #genre
				oaiso_genre = Shop_info.objects.all().filter(id=shop_id).values_list('oaiso_genre', flat=True) #oaiso_genre
				lat = Shop_info.objects.all().filter(id=shop_id).values_list('lat', flat=True) #lat
				lng = Shop_info.objects.all().filter(id=shop_id).values_list('lng', flat=True) #lng
				address = Shop_info.objects.all().filter(id=shop_id).values_list('address', flat=True) #address
				budget_lunch_min = Shop_info.objects.all().filter(id=shop_id).values_list('budget_lunch_min', flat=True)
				budget_lunch_max = Shop_info.objects.all().filter(id=shop_id).values_list('budget_lunch_max', flat=True)
				budget_dinner_min = Shop_info.objects.all().filter(id=shop_id).values_list('budget_dinner_min', flat=True)
				budget_dinner_max = Shop_info.objects.all().filter(id=shop_id).values_list('budget_dinner_max', flat=True)

				sim_score = cos_sim(user_vec[3:8], shop_vec) #cos類似度のスコア
				dist_score = (dist_ref - shop_dist)/dist_ref #距離スコア
				oaiso_score = math.sqrt(sim_score*sim_score + dist_score*dist_score) #総合スコア

				score_list.append(
					[uvec_str, 
					svec_str, 
					dist_score, 
					shop_dist,
					sim_score, 
					oaiso_score, 
					str(shop_id), 
					list(shop_name)[0], 
					list(links)[0],
					list(genre)[0],
					list(oaiso_genre)[0],
					list(lat)[0],
					list(lng)[0],
					list(address)[0],
					list(budget_lunch_min)[0],
					list(budget_lunch_max)[0],
					list(budget_dinner_min)[0],
					list(budget_dinner_max)[0]]
					)
		
		score_list = list(map(list, set(map(tuple, score_list))))
		return sorted(score_list, key=lambda x:x[5], reverse=True)  #oaiso_score順に並び替える


	elif user_vec[2] != 0: #価格帯が高いとき
		for row in d_sorted:
			shop_id = row[0] #店のid
			shop_dist = row[1] #店の距離

			for label in Label_first.objects.all().filter(id=shop_id).filter(~Q(budget_expensive = 0)).values_list():
				list_label = list(label)

				shop_vec = np.array(list_label[4:9])	#飲食店の特徴ベクトル(NumPy配列)
				svec_str = ','.join([str(i) for i in (list_label[1:])]) #特徴ベクトル文字列
				shop_name = Shop_info.objects.all().filter(id=shop_id).values_list('shop_name', flat=True) #shop_name
				links = Shop_info.objects.all().filter(id=shop_id).values_list('links', flat=True) #links
				genre = Shop_info.objects.all().filter(id=shop_id).values_list('genre', flat=True) #genre
				oaiso_genre = Shop_info.objects.all().filter(id=shop_id).values_list('oaiso_genre', flat=True) #oaiso_genre
				lat = Shop_info.objects.all().filter(id=shop_id).values_list('lat', flat=True) #lat
				lng = Shop_info.objects.all().filter(id=shop_id).values_list('lng', flat=True) #lng
				address = Shop_info.objects.all().filter(id=shop_id).values_list('address', flat=True) #address
				budget_lunch_min = Shop_info.objects.all().filter(id=shop_id).values_list('budget_lunch_min', flat=True)
				budget_lunch_max = Shop_info.objects.all().filter(id=shop_id).values_list('budget_lunch_max', flat=True)
				budget_dinner_min = Shop_info.objects.all().filter(id=shop_id).values_list('budget_dinner_min', flat=True)
				budget_dinner_max = Shop_info.objects.all().filter(id=shop_id).values_list('budget_dinner_max', flat=True)

				sim_score = cos_sim(user_vec[3:8], shop_vec) #cos類似度のスコア
				dist_score = (dist_ref - shop_dist)/dist_ref #距離スコア
				oaiso_score = math.sqrt(sim_score*sim_score + dist_score*dist_score) #総合スコア

				score_list.append(
					[uvec_str, 
					svec_str, 
					dist_score, 
					shop_dist,
					sim_score, 
					oaiso_score, 
					str(shop_id), 
					list(shop_name)[0], 
					list(links)[0],
					list(genre)[0],
					list(oaiso_genre)[0],
					list(lat)[0],
					list(lng)[0],
					list(address)[0],
					list(budget_lunch_min)[0],
					list(budget_lunch_max)[0],
					list(budget_dinner_min)[0],
					list(budget_dinner_max)[0]]
					)
		
		score_list = list(map(list, set(map(tuple, score_list))))	
		return sorted(score_list, key=lambda x:x[5], reverse=True)  #oaiso_score順に並び替える




"""
if __name__ == '__main__':
	lat = 35.691638   #緯度
	lng = 139.704616  #経度
	uvec = [0,1,0,0,1,0,0,1,0]  #ユーザベクトル

	dist = distance_filter(lat, lng)
	results = contents_filter(dist, uvec)[:10]

	for row in results:
		print('\t'.join([str(i) for i in row]))
"""


