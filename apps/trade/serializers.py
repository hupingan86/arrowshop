from rest_framework import serializers
from .models import ShoppingCart
from goods.models import Goods
from goods.serializers import GoodsSerializer


# 购物车列表详情
class ShopCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)

    class Meta:
        model = ShoppingCart
        fields = "__all__"


class ShopCartSerializer(serializers.Serializer):  # 要用Serializer方法

    # 把表里面的字段映射过来
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    nums = serializers.IntegerField(required=True, label="数量", min_value=1,
                                    error_messages={
                                        "min_value": "商品数量不能小于1",
                                        "required": "请选择购买数量"
                                    })
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    # 商品数量进行添加
    def create(self, validated_data):
        user = self.context["request"].user   # 获取当前登录的用户
        nums = validated_data["nums"]
        goods = validated_data["goods"]

        existed = ShoppingCart.objects.filter(user=user, goods=goods)    # 查询是否有这条记录

        # 如果存在了
        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)
        return existed

    def update(self, instance, validated_data):
        # 修改商品数量   instance相当于ShopCartViewSet的实例
        instance.nums = validated_data["nums"]
        instance.save()
        return instance



