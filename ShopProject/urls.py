"""ShopProject URL Configuration

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
import xadmin
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from ShopProject.settings import MEDIA_ROOT
from app.goods.views import GoodsListViewSet, CategoryViewSet, BannerViewset

# #绑定get方法和list函数
# goods_list = GoodsListViewSet.as_view({ 'get': 'list', })

#自动生成路由和函数的对应关系
from app.trade.views import ShoppingCartViewset, OrderViewset, AlipayView
from app.user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from app.users.views import SmsCodeViewset, UserViewset

router = DefaultRouter() # 配置goods的url, 自动生成路由
router.register(r'goods', GoodsListViewSet, basename='goods')   #商品页面url
router.register(r'categorys', CategoryViewSet, basename="categorys")  #商品分类页面url
router.register(r'code', SmsCodeViewset, basename="code")
router.register(r'users', UserViewset, basename="users")
#配置用户收藏的url
router.register(r'userfavs', UserFavViewset, basename="userfavs")
#配置用户留言的url，basename--->通过别名反向查找路由地址
router.register(r'messages', LeavingMessageViewset, basename="messages")
# 配置收货地址
router.register(r'address', AddressViewset, basename="address")
#配置购物车url
router.register(r'shopcarts', ShoppingCartViewset, basename="shopcarts")
#配置订单的url
router.register(r'orders', OrderViewset, basename="orders")
#轮播图url
router.register(r'banners', BannerViewset, basename="banners")

urlpatterns = [
    #path('admin/', admin.site.urls),
    #使用xadmin进行后台管理
    path('xadmin/', xadmin.site.urls),
    #富文本编辑时的路由配置
    path('ueditor/', include('DjangoUeditor.urls')),
    #文件,通过路由方式访问用户上传的文件/图片/视频
    path('media/<path:path>',serve,{'document_root': MEDIA_ROOT}),

    #商品列表页
    #path('goods1/',GoodsListView.as_view(),name='goods-list-django'),

    path('api-auth/',include('rest_framework.urls')),

    # drf文档，title自定义, 如果要实现API文档页展示，需要在settings文件中配置。
    path('docs',include_docs_urls(title='Fan RESTful Docs')),
    #商品列表页, 删除前两种商品列表页的url配置.
    # path('goods/',goods_list,name='goods-list-rest')

    #REST token 路由配置
    #path('api-token-auth/', views.obtain_auth_token),
    #jwt token 路由配置
    path('jwt-auth/', obtain_jwt_token),

    #配置支付宝的url。
    path('alipay/return/', AlipayView.as_view())
]

# 将DefaultRouter注册的路由和视图函数对应关系添加到urlpatterns里面。
urlpatterns += router.urls