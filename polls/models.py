#coding=UTF-8
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __repr__(self):
        return self.question.decode('utf-8')

    def was_publish(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1)<=self.pub_date <=now

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __repr__(self):
        return self.choice_text

class User(models.Model):
    username = models.CharField('账号',max_length=100)
    password = models.CharField('密码', max_length=100)
    age = models.CharField('年龄', max_length=20)
    addr = models.CharField('地址', max_length=200)
    def __repr__(self):
        return self.username
