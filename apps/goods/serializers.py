from rest_framework import serializers
from goods.models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    """
    商品类别序列化，第三类
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """
    商品类别序列化，第二类
    """
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化 ,第一类
    """

    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()   # 商品序列化

    class Meta:
        model = Goods
        fields = "__all__"
