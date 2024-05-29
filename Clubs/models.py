from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime

class Club(models.Model):
  club_id = models.AutoField(primary_key=True)
  club_name = models.CharField(max_length=100)
  club_time = models.CharField(max_length=100) 
  club_introduction = models.CharField(max_length=100)
  club_details = models.CharField(max_length=100)
  club_contact = models.CharField(max_length=100)
  club_open = models.BooleanField()
  club_open_start = models.DateField(max_length=100)
  club_open_end = models.DateField(max_length=100)
  club_code = models.CharField(max_length=100)
  club_pic = models.ImageField(null=True, blank=True)


  # django는 모델에 하나의 AutoField만 허용
  # 기본적으로 Django 모델에 기본 키로 id Field를 추가하므로 club_id 필드를 AutoField로 설정하고 싶다면,
  # id Field를 club_id Field로 대체
  def __str__(self):
      return self.club_name

  # 동아리 신청 남은 일 수 계산
  def remaining_days(self):
    days = ("D-" + str((self.club_open_end - datetime.now().date()).days))
    return days