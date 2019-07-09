from django.db import models

class Level(models.Model):
  id = models.AutoField(primary_key=True)
  kup = models.IntegerField(default=0)
  name = models.CharField(max_length=100)

class MainList(models.Model):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateField(null=True)
  level = models.ForeignKey(Level, on_delete=models.CASCADE,null=True)
  sex = models.CharField(max_length=1,null=True)

class Fee(models.Model):
  player_id = models.ForeignKey(MainList, on_delete=models.CASCADE)
  january = models.BooleanField(default=False)
  february = models.BooleanField(default=False)
  march = models.BooleanField(default=False)
  april = models.BooleanField(default=False)
  may = models.BooleanField(default=False)
  june = models.BooleanField(default=False)
  september = models.BooleanField(default=False)
  october = models.BooleanField(default=False)
  november = models.BooleanField(default=False)
  december = models.BooleanField(default=False)

class Payments(models.Model):
  player_id = models.ForeignKey(MainList, on_delete=models.CASCADE,default=0)
  value = models.IntegerField(null=True)
  month = models.CharField(max_length=50)
  year = models.CharField(max_length=4)
