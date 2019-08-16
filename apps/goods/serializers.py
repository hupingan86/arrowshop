from rest_framework import serializers
from goods.models import Goods, GoodsCategory, GoodsImage
from django.db.models import Q


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


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()   # 商品序列化
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"


class IndexCategorySerializer(serializers.ModelSerializer):
    goods = serializers.SerializerMethodField()
    sub_cat = CategorySerializer2(many=True)
    ad_goods = serializers.SerializerMethodField()

    def get_goods(self, obj):
        all_goods = Goods.objects.filter(Q(category_id=obj.id) | Q(category__parent_category_id=obj.id) |
                                         Q(category__parent_category__parent_category_id=obj.id))
        goods_serializer = GoodsSerializer(all_goods, many=True, context={'request': self.context['request']})
        return goods_serializer.data

    def get_ad_goods(self, obj):
        pass

        # goods_json = {}
        # ad_goods = IndexAd.objects.filter(category_id=obj.id)
        # if ad_goods:
        #     good_ins = ad_goods[0].goods
        #     # context 上下文加上域名
        #     goods_json = GoodsSerializer(good_ins, many=False, context={'request': self.context['request']}).data
        # return goods_json

    class Meta:
        model = GoodsCategory
        fields = "__all__"