from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # to rename sale_price to discount, discount need's method get_discount
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product  # one model can have multiple serializer with diff application
        fields = [
            'title',    # this fild only require, while validating for Product model
            'content',  # content is blank=True, null=True so doesn't matter if we pass or not
            'price',    # price has default=99.99 value so same here also
            'discount', # renamed sale_price -> discount
        ] # in serializer.data will give only values witch we have passed
          # and content also because it is blank=True or null=True
          # and discount because it externally defined in ProductSerializer
    def get_discount(self, obj):
        if not isinstance(obj, Product):
            # when obj is not instance of Product class then obj can not access class models properties
            # so handled using this
            return None
        if not hasattr(obj, 'id'):  # this is help also
            return None
        return obj.sale_price