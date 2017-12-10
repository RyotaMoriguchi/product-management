from django.conf.urls import url

from pro import views

urlpatterns = [
    # 商品
    url(r'^index/$', views.product_list, name='product_list'),   # 一覧
    #url(r'^product/add/$', views.product_regist, name='product_add'), # 登録
    ]
