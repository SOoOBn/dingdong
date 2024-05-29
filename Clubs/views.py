from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from .models import Club
from rest_framework.permissions import IsAuthenticated

class ClubAPIView(APIView):
    permission_classes = [IsAuthenticated] # 인증된 사용자만 접근 가능

    def post(self, request):
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            club = serializer.save()
            remaining_days = club.remaining_days()
            return Response(
            { 
            "message": "Club registered successfully.",
            "club_id": club.club_id,
            "remaining_days": remaining_days
            }
            )
        
        return Response(serializer.errors)

class ClubListAPIView(APIView):
    def get(self,request):
      clubs = Club.objects.all()
      serializer = ClubListSerializer(clubs, many=True)
      return Response({"clubs": serializer.data})
