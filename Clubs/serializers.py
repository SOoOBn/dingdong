from rest_framework import serializers
from .models import Club
from Users.models import User

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class ClubBaseSerializer(serializers.ModelSerializer):
    club_id = serializers.CharField(max_length=100)
    club_name = serializers.CharField(max_length=100)
    club_time = serializers.CharField(max_length=100) 
    club_introduction = serializers.CharField(max_length=100)
    club_details = serializers.CharField(max_length=100)
    club_contact = serializers.CharField(max_length=100)
    club_open = serializers.BooleanField()
    club_open_start = serializers.CharField(max_length=100)
    club_open_end = serializers.CharField(max_length=100)
    club_code = serializers.CharField(max_length=100)
    club_pic = serializers.ImageField()

    def create(self, validated_data):
        club = Club.objects.create(
          club_id = validated_data['club_id'],
          club_name = validated_data['club_name'],
          club_time = validated_data['club_time'],
          club_introduction = validated_data['club_introduction'],
          club_details = validated_data['club_details'],
          club_open_start = validated_data['club_open_start'],
          club_open_end = validated_data['club_open_end'],
          club_code = validated_data['club_code'],
          )
        return club

class ClubListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['club_id', 'club_name', 'club_introduction', 'club_open', 'remaining_days']



  


    