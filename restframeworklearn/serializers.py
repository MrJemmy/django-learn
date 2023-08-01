from rest_framework import serializers
from .models import Product

def check_length(value):
    """
    This is call validators
    writen to validate command validations for all columns or fields
    we can write this in Serializer class also
    """
    if len(value)<5 and (value!=None or value!=''):
        raise serializers.ValidationError('This Title can not be crated, no of char should at list 5')


class ProductModelSerializer(serializers.ModelSerializer):
    # to rename sale_price to discount, discount need's method get_discount
    discount = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[check_length])
    class Meta:
        model = Product  # one model can have multiple serializer with diff application
        fields = [
            'title',    # this fild only require, while validating for Product model
            'content',  # content is blank=True, null=True so doesn't matter if we pass or not
            'price',    # price has default=99.99 value so same here also
            'discount', # renamed function sale_price -> discount
        ] # in serializer.data will give only values witch we have passed
          # allways it will return content because it is blank=True or null=True
          # and discount because it externally defined in ProductSerializer
        read_only_fields = ['price'] # with This we can not insert/update data for this fields
        # extra_kwargs = {'price':{'read_only':True}} # we can use this also

    def get_discount(self, obj):
        if not isinstance(obj, Product) or not hasattr(obj, 'id'):
            # when obj is not instance of Product class then obj can not access class's models properties
            # obj dones not have an attribute 'id' then also we can say something is wrong with 'obj'
            # 'obj' is not instance of Product class
            return None
        return obj.sale_price

    def validate_title(self, value):
        """
        Fild level validation
        This method is automatic called when "is_valid()" method is called.
        """
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('This Title is already exist')
        return value

    def validate(self, data):
        """
        object level validation
        to validate internal conditions or group conditions
        """
        title = data.get('title', None)
        content = data.get('content', None)
        if title == content:
            raise serializers.ValidationError('title and content can not be of same name')
        return data


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=160, validators=[check_length])
    content = serializers.CharField(max_length=160, default=None) # allow_blank=True, allow_null=True ? does not work
    price = serializers.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content',  instance.content)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    # Validations
    def validate_title(self, value):
        """
        Fild level validation
        This method is automatic called when "is_valid()" method is called.
        """
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('This Title is already exist')
        return value

    def validate(self, data):
        """
        object level validation
        to validate internal conditions or group conditions
        """
        title = data.get('title', None)
        content = data.get('content', None)
        if title == content:
            raise serializers.ValidationError(' ')
        return data
