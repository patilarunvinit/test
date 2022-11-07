from django.db import models

# Create your models here.

class vinfo(models.Model):
    vno = models.IntegerField()
    area = models.CharField(max_length=150)
    ward = models.CharField(max_length=10)
    mr_fname = models.CharField(max_length=75)
    mr_mname = models.CharField(max_length=75)
    mr_lname = models.CharField(max_length=75)
    eng_fname = models.CharField(max_length=75)
    eng_mname = models.CharField(max_length=75)
    eng_lname = models.CharField(max_length=75)
    vstatus = models.CharField(max_length=75)
    kayperson = models.IntegerField()
    value = models.CharField(max_length=50)
    wk = models.CharField(max_length=50)
    stg = models.CharField(max_length=50)
    is_cand = models.CharField(max_length=1)
    addr = models.CharField(max_length=250)
    con_yn = models.CharField(max_length=1)
    bhv = models.CharField(max_length=100)
    family_org = models.CharField(max_length=25)
    rel_1 = models.CharField(max_length=50)
    rel_2 = models.CharField(max_length=50)
    rmk = models.CharField(max_length=150)


    objects = models.Manager()