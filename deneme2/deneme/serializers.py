from .models import Word,Kullanici,Mean
from rest_framework import serializers


class wordsserializer(serializers.ModelSerializer):
    class Meta:
        model=Word
        fields=['id','name','means','kullanici']

# class WordSerializer(serializers.Serializer):
#
#     id=serializers.IntegerField()
#     name=serializers.CharField()
#     means=serializers.StringRelatedField()
#     kullanici=serializers.StringRelatedField()
#
#     def create(self, validated_data):
#
#         kullanici1=Kullanici.objects.get(id=2)
#         name1=validated_data.get('name')
#         id1=validated_data.get('id')
#         word=Word(id=id1,name=name1,kullanici=kullanici1)
#         word.save()
#
#         return word
#
#     def update(self, instance, validated_data):
#         """
#         Güncelleme vs. yapıldığındada aynı şekil yansıyacaktır.
#         """
#         instance.name=validated_data.get('name',instance.name)
#         instance.id=validated_data.get('id',instance.id)
#         instance.save()
#         return instance

# class KullaniciSerializer(serializers.Serializer):
#         id=serializers.IntegerField()
#         userName = serializers.CharField()
#         password=serializers.CharField()
#         kullanicininkelimesi=serializers.StringRelatedField()
#
#         def create(self, validated_data):
#             """
#             Yeni veri eklendiğinde, aynı şekilde yansıyacaktır.
#             """
#             return Kullanici.objects.create(**validated_data)
#
#         def update(self, instance, validated_data):
#             """
#             Güncelleme vs. yapıldığındada aynı şekil yansıyacaktır.
#             """
#             instance.name = validated_data.get('name', instance.name)
#             instance.kullanicininkelimesi = ('kullanicininkelimesi', instance.kullanicininkelimesi)
#             instance.save()
#             return instance
#

class meanserializer(serializers.ModelSerializer):
    class Meta:
        model = Mean
        fields = ['id', 'meanName', 'word']

class kullaniciserializer(serializers.ModelSerializer):
    class Meta:
        model = Kullanici
        fields = ['id', 'userName', 'password']

