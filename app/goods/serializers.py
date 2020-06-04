#coding:utf-8
#date:2020/5/618:21
#author:CQ_Liu
from rest_framework import serializers

from app.goods.models import Goods, GoodsCategory, GoodsImage, Banner

"""
方法一：serializers序列化
"""
# class GoodsSerializer(serializers.Serializer):
# #     name = serializers.CharField(required=True,max_length=100)
# #     click_num = serializers.IntegerField(default=0)
# #     goods_front_image = serializers.ImageField()
"""
方法二：ModelSerializer序列化，可以自动序列化数据库模型所有信息,
        通过exclude取消不需要序列化的字段
"""

from rest_framework import serializers

class CategorySerializer3(serializers.ModelSerializer):
    '''三级分类'''
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    ''' 二级分类 '''
    # 在parent_category字段中定义的related_name="sub_cat"
    # many=True代表子分类有多个。否则会报错。
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """一级分类序列化"""
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    """轮播图"""
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 ，不指定时只显示分类的id
    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        #fields = '__all__'  #all返回所有字段
        exclude = ['goods_desc',]  #不需要序列化的字段

class BannerSerializer(serializers.ModelSerializer):
    ''' 轮播图 '''
    class Meta:
        model = Banner
        fields = "__all__"


