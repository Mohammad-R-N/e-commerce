from rest_framework.serializers import ModelSerializer
from games.models import Games,Category,Creator


class GamesSerializer(ModelSerializer):

    class Meta:
        model = Games
        fields = ["id", "title", "image", "summary",'console',"release_time","price","players","is_online","category","creator"]


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class CreatorSerializer(ModelSerializer):

    class Meta:
        model = Creator
        fields = ["id", "name"]