from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from oaiso import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^shops$', views.shops),
    url(r'^shop_info$', views.shop_info),
]

