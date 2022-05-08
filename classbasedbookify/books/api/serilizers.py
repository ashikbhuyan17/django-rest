from rest_framework import serializers
from books.models import Books
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.IntegerField()
    in_stock = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.in_stock = validated_data.get('in_stock', instance.in_stock)
        instance.save()
        return instance
