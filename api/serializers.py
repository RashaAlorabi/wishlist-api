from rest_framework import serializers
from items.models import Item ,FavoriteItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',]


class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    users_num_item = serializers.SerializerMethodField()
    added_by = UserSerializer()
    class Meta:
        model = Item
        fields = [
            'name',
            'detail',
            'added_by',
            'users_num_item',
            ]
    def  get_users_num_item(self,obj):
        return obj.favoriteitem_set.count()


class ItemDetailSerializer(serializers.ModelSerializer):
    favorited_by = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = '__all__'
    def get_favorited_by(self, obj):
        return "%s %s"%(obj.added_by.first_name, obj.added_by.last_name)    


