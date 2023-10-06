from rest_framework.serializers import ModelSerializer
from cart.models import Cart,OrderItem


class CartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = ["id", "total_price", "time", "total_quantity",'status']


class OrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ["id", "games", "cart", "quantity",'price']

