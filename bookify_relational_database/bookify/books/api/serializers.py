
from rest_framework import serializers

from books import models

# validators 
# def check_title(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('length must be more than 2')

class BooksSerializer(serializers.ModelSerializer):
    # title_and_price = serializers.SerializerMethodField()
    class Meta:
        model = models.BookList
        fields = '__all__'
        depth = 1
        # exclude = ['price']


class SellingPlatformSerializer(serializers.ModelSerializer):
    #  booklists means model related_name
    # book-details => urls name => ami jey urls refer name er details dekathe cachi
    # Writable nested serializers
    booklists = BooksSerializer(
        many=True,
        # read_only=True,
        # view_name='book-details'
    )
    class Meta:
        model = models.SellingPlatform
        fields = '__all__'




























    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(validators=[check_title])
    # description = serializers.CharField()
    # price = serializers.IntegerField()
    # in_stock = serializers.BooleanField()


    # def create(self,validated_data):
    #     return models.Books.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title',instance.title)
    #     instance.description = validated_data.get('description',instance.description)
    #     instance.price = validated_data.get('price',instance.price)
    #     instance.in_stock = validated_data.get('in_stock',instance.in_stock)
    #     instance.save()
    #     return instance

    # field level
    # def validate_price(self,value):
    #     if value<=1:
    #         raise serializers.ValidationError('price must be greater than 1 !!')
    #     return value
    # object level 
    # def validate(self,data):
    #     if data['title'].lower() and data['description'].lower():
    #         raise serializers.ValidationError('title and description can not be lower')
    #     return data



