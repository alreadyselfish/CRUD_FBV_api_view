from rest_framework import serializers
from api.models import Product 

class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = Product 
        fields = ['id', 'name', 'desc', 'price', 'discounted_price']
    
    def get_discounted_price(self, instance):
        dp = float(instance.price) * 0.78
        return str(round(dp, 3))

