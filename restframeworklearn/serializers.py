from rest_framework import serializers
from .models import Product


class ProductModelSerializer(serializers.ModelSerializer):
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
        if not isinstance(obj, Product) or not hasattr(obj, 'id'):
            # when obj is not instance of Product class then obj can not access class's models properties
            # obj dones not have attribute 'id' then also we can say something is wrong with 'obj'
            # 'obj' is not instance of Product class
            return None
        return obj.sale_price


def check_length(value):
    """
    This is call validators
    writen to validate command validations for all columns or filds
    """
    if len(value)<5 and (value!=None or value!=''):
        raise serializers.ValidationError('This Title can not be crated')

class ProductSerializer(serializers.Serializer):
    """
    : to get data using GET method
    query = Model.objects.all()
    serializer = ProductSerializer(query, many=True)  # get All data
    return JsonResponse(serializer.data)

    query = Model.objects.get(pk=pk)
    serializer = ProductSerializer(query)  # while getting single data
    return JsonResponse(serializer.data)

    : to delete data : for this we do not need "Serializer"
    query = Model.objects.get(pk=pk)
    query.delete()
    """
    title = serializers.CharField(max_length=160, validators=[check_length])
    content = serializers.CharField(max_length=160, default=None) # allow_blank=True, allow_null=True ? does not work
    price = serializers.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    def create(self, validated_data):
        """
        : To Insert data into DB, Here we have to create method for insertion
        : It will use POST method.
        data = request.data
        serializers = ProductSerializer(data=data)  # **need to write data=data
        if serializers.is_valid():
            serializers.save() to create data
        else:
            print(serializer.errors)
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        : How to call:
        : It will use PUT method.
        data = request.body
        pk = data.get('pk', None)
        query = Model.objects.get(pk=pk)
        serializers = ProductSerializer(query, data=data)  # to update whole data
        serializers = ProductSerializer(query, data=data, partial=True)  # to update partial data
        if serializers.is_valid():
            serializers.save() it will update data
        else:
            print(serializer.errors)
        """
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
        qs = Product.objects.filter(title__icontains=value)
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
