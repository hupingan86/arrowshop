"""arrowshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from arrowshop.settings import MEDIA_ROOT
from django.urls import path, re_path
from django.views.static import serve
from django.conf.urls import include, url
import xadmin

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from users.views import UserViewSet
from goods.views import GoodsListViewSet, CategoryViewSet, IndexCategoryViewSet
from user_operation.views import AddressViewSet
from trade.views import ShoppingCartViewSet

from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
# 用户的
router.register(r'users', UserViewSet, base_name="users")
# 商品的情况
router.register(r'goods', GoodsListViewSet, base_name="goods")
# 商品分类
router.register(r'categorys', CategoryViewSet, base_name="categorys")
# 收获地址
router.register(r'address', AddressViewSet, base_name="address")

# 首页分类商品url
router.register(r'indexgoods', IndexCategoryViewSet, base_name="indexgoods")

# 购物车url
router.register(r'shopcarts', ShoppingCartViewSet, base_name="shopcarts")

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path('^', include(router.urls)),
    re_path('^login/', obtain_jwt_token),  # 登录接口
]
