from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from oaiso.models import Shop, Shop_info
from oaiso import recommend #, recommend_backup
from oaiso.serializers import UserSerializer, GroupSerializer, ShopSerializer, TestSerializer
import random
from django.http import HttpResponse, HttpResponseNotFound

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



def shops(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return JsonResponse(serializer.data, safe=False)


def shop_info(request):
    if request.GET.get('lat') and request.GET.get('lng') and request.GET.get('uvec'):
        req_lat = request.GET['lat']    #緯度のリクエストパラメータ
        req_lng = request.GET['lng']    #経度のリクエストパラメータ
        uvec = request.GET['uvec'] #ユーザベクトルのリクエストパラメータ
        list_uvec = list(map(float, uvec.split(",")))
        r = 800  #エリアの距離(初期値)

        #レコメンドロジックの実行処理
        dref, d =  recommend.distance_filter(r, req_lat, req_lng) #距離フィルタリング
        recommend_id = recommend.contents_filter(dref, d, list_uvec) #内容ベースフィルタリング
        

        #提案店舗データ
        shop_info = Shop_info.objects.all().filter(id__in=recommend_id[:5]).extra(
            select={'manual': 'FIELD(id,%s)' % ','.join(map(str, recommend_id))},
            order_by=['manual'])
        

        #Jsonに変換
        serializer = TestSerializer(shop_info, many=True)
        return JsonResponse(serializer.data, safe=False)


    else:
        shop_info = Shop_info.objects.all()
        serializer = TestSerializer(shop_info, many=True)

    return JsonResponse(serializer.data, safe=False)

