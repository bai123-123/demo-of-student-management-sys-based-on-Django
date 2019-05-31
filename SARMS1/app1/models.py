from django.db import models

# Create your models here.


class Account(models.Model):

    account_m = models.CharField(max_length=32)

    pwd = models.CharField(max_length=32)

class Students(models.Model):

    student_ID = models.IntegerField(primary_key=True)

    student_name = models.CharField(max_length=32)

    student_AP = models.ForeignKey('AP')

    student_FC = models.ForeignKey('FC')

class AP(models.Model):
    AP_id = models.IntegerField(primary_key=True)

    week1_p = models.CharField(max_length=3,null=True, blank=True)
    week1_A = models.CharField(max_length=3,null=True, blank=True)
    week2_p = models.CharField(max_length=3,null=True, blank=True)
    week2_A = models.CharField(max_length=3, null=True, blank=True)
    week3_p = models.CharField(max_length=3,null=True,blank=True)
    week3_A = models.CharField(max_length=3,null=True,blank=True)
    week4_p = models.CharField(max_length=3,null=True,blank=True)
    week4_A = models.CharField(max_length=3,null=True,blank=True)
    week5_p = models.CharField(max_length=3,null=True,blank=True)
    week5_A = models.CharField(max_length=3,null=True,blank=True)
    week6_p = models.CharField(max_length=3,null=True,blank=True)
    week6_A = models.CharField(max_length=3,null=True,blank=True)
    week7_p = models.CharField(max_length=3,null=True,blank=True)
    week7_A = models.CharField(max_length=3,null=True,blank=True)
    week8_p = models.CharField(max_length=3,null=True,blank=True)
    week8_A = models.CharField(max_length=3,null=True,blank=True)
    week9_p = models.CharField(max_length=3,null=True,blank=True)
    week9_A = models.CharField(max_length=3,null=True,blank=True)
    week10_p = models.CharField(max_length=3,null=True,blank=True)
    week10_A = models.CharField(max_length=3,null=True,blank=True)


class FC(models.Model):
    sutdend_ID = models.IntegerField
    feedback = models.CharField(blank=True,max_length=300)

    comments = models.CharField(blank=True,max_length=300)

class units(models.Model):

    unit_ID = models.IntegerField
    student_ID = models.IntegerField