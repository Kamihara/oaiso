from oaiso.models import Shop_info, Label_first, Shop_label
from django.db.models import Q
import pyproj
import numpy as np


def sample():
	id_list = Label_first.objects.values_list('id', flat=True).order_by('id')
	return id_list

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
def distance_filter(req_lat, req_lng):
	dist_list = []
	distance_list = return_distance(req_lat, req_lng) #店のidと現在地からの距離のリスト

	#現在地から徒歩10分(半径800m)以内にある店のidを取り出す
	for row in distance_list:
		if row[1] <= 800:
			dist_list.append([row[0], row[1]])

	if len(dist_list) >= 100:	#店舗数が100件以上の時はdist_listを返す
		return dist_list

	else:
		return distsort(distance_list)[:100]  #100件未満の時は近い順に並べた100件のidと距離を返す


# 内容ベースフィルタリング関数
def contents_filter(dlist, uvec):
	score_list = []	#oaisoスコアのリスト初期化
	user_vec = np.array(uvec)	#ユーザベクトル(user_vec)をNumPy配列で受け取り
	d_sorted = sorted(dlist, key=lambda x:x[0]) #dlistをid順に並び替え
	distance = 200

	#飲食店のラベリングデータの呼び出し
	if user_vec[0] != 0: #価格帯が低いとき
		for row in d_sorted:
			shop_id = row[0] #店のid
			shop_dist = row[1] #店の距離

			for label in Shop_label.objects.all().filter(id=shop_id).filter(~Q(budget_cheap = 0)).values_list():
				list_label = list(label)

				shop_vec = np.array(list_label[4:])	#飲食店の特徴ベクトル(NumPy配列)
				weight = [5, 5, 5, 5, 1, 1] #ベクトルの各要素にのみ重みを付けるNumPy特有の係数(※ベクトルではない)

				sim_score = cos_sim(user_vec[3:], shop_vec * weight) #cos類似度のスコア
				dist_score = (800 - shop_dist)/800 #距離のスコア

				#oaisoスコア
				if dist_score > 0:
					if sim_score * sim_score > 0.2:
						oaiso_score = sim_score * sim_score + dist_score
					else:
						oaiso_score = sim_score * sim_score
				else:
					oaiso_score = sim_score * sim_score

				score_list.append([shop_id, oaiso_score])	#飲食店のidとoaisoスコアが入った二次元リストを作成

		return return_id(score_list)	#oaisoスコア順に並び替えたidを返す

	
	elif user_vec[1] != 0: #価格帯が中のとき
		while True:
		for row in d_sorted:
			shop_id = row[0] #店のid
			shop_dist = row[1] #店の距離

			for label in Shop_label.objects.all().filter(id=shop_id).filter(~Q(budget_reasonable = 0)).values_list():
				list_label = list(label)

				shop_vec = np.array(list_label[4:])	#飲食店の特徴ベクトル(NumPy配列)
				weight = [5, 5, 5, 5, 1, 1] #ベクトルの各要素にのみ重みを付けるNumPy特有の係数(※ベクトルではない)


				sim_score = cos_sim(user_vec[3:], shop_vec * weight) #cos類似度のスコア
				dist_score = (800 - shop_dist)/800 #距離のスコア

				#oaisoスコア
				if dist_score > 0:
					if sim_score * sim_score > 0.2:
						oaiso_score = sim_score * sim_score + dist_score
					else:
						oaiso_score = sim_score * sim_score
				else:
					oaiso_score = sim_score * sim_score

				score_list.append([shop_id, oaiso_score])	#飲食店のidとoaisoスコアが入った二次元リストを作成

		return return_id(score_list)	#oaisoスコア順に並び替えたidを返す

	
	elif user_vec[2] != 0: #価格帯が高いとき
		for row in d_sorted:
			shop_id = row[0] #店のid
			shop_dist = row[1] #店の距離

			for label in Shop_label.objects.all().filter(id=shop_id).filter(~Q(budget_expensive = 0)).values_list():
				list_label = list(label)

				shop_vec = np.array(list_label[4:])	#飲食店の特徴ベクトル(NumPy配列)
				weight = [5, 5, 5, 5, 1, 1] #ベクトルの各要素にのみ重みを付けるNumPy特有の係数(※ベクトルではない)

				sim_score = cos_sim(user_vec[3:], shop_vec * weight) #cos類似度
				dist_score = (800 - shop_dist)/800 #距離スコア
				
				#oaisoスコア
				if dist_score > 0:
					if sim_score * sim_score > 0.2:
						oaiso_score = sim_score * sim_score + dist_score
					else:
						oaiso_score = sim_score * sim_score
				else:
					oaiso_score = sim_score * sim_score

				score_list.append([shop_id, oaiso_score])	#飲食店のidとoaisoスコアが入った二次元リストを作成

		return return_id(score_list)	#oaisoスコア順に並び替えたidを返す

	else:
		pass








