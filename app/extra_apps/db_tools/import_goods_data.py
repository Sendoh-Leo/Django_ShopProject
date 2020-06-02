# -*- coding: utf-8 -*-


import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ShopProject.settings")

import django

django.setup()
#注意：导入数据库模型，一定要先加载Django配置和Django App
from app.goods.models import Goods, GoodsCategory, GoodsImage
from app.extra_apps.db_tools.data.product_data import row_data

# 依次遍历商品信息
for goods_detail in row_data:
    # 实例化商品对象;
    goods = Goods()
    goods.name = goods_detail["name"]
    #将￥232元处理为232
    goods.market_price = float((goods_detail["market_price"].replace("￥", "").replace("元", "")))
    goods.shop_price = float((goods_detail["sale_price"].replace("￥", "").replace("元", "")))

    goods.goods_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""
    goods.goods_desc = goods_detail["goods_desc"] if goods_detail["goods_desc"] is not None else ""

    #将商品轮播图第一张图片作为哦商品列表页显示的图片
    goods.goods_front_image = goods_detail["images"][0] if goods_detail["images"] else ""

    #将商品和商品分类关联，只关联三级分类（可以根据三级分类找到一级二级分类）
    # 商品的三级分类
    category_name = goods_detail["categorys"][-1]
    #根据分类名称找到分类对象，因为商品类别关联的是类别对象，不是类别名称
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()
    print("添加商品 [%s] 成功" % (goods.name))

    # 添加商品图片
    for goods_image in goods_detail["images"]:
        #创建商品轮播图对象
        goods_image_instance = GoodsImage()
        goods_image_instance.image = goods_image
        #将商品轮播图对象与商品对象邦栋
        goods_image_instance.goods = goods
        goods_image_instance.save()
