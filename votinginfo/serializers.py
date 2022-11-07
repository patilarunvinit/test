from .models import vinfo
from rest_framework import serializers


class infoserializer(serializers.Serializer):
    id = serializers.IntegerField()
    vno = serializers.IntegerField()
    area = serializers.CharField(max_length=150)
    ward = serializers.CharField(max_length=10)
    mr_fname = serializers.CharField(max_length=75)
    mr_mname = serializers.CharField(max_length=75)
    mr_lname = serializers.CharField(max_length=75)
    eng_fname = serializers.CharField(max_length=75)
    eng_mname = serializers.CharField(max_length=75)
    eng_lname = serializers.CharField(max_length=75)
    vstatus = serializers.CharField(max_length=75)
    kayperson = serializers.IntegerField()
    value = serializers.CharField(max_length=50)
    wk = serializers.CharField(max_length=50)
    stg = serializers.CharField(max_length=50)
    is_cand = serializers.CharField(max_length=1)
    addr = serializers.CharField(max_length=250)
    con_yn = serializers.CharField(max_length=1)
    bhv = serializers.CharField(max_length=100)
    family_org = serializers.CharField(max_length=25)
    rel_1 = serializers.CharField(max_length=50)
    rel_2 = serializers.CharField(max_length=50)
    rmk = serializers.CharField(max_length=150)

    class Meta:
        model = vinfo
        felds = ("id","vno","area","ward","mr_fname","mr_mname","mr_lname","eng_fname","eng_mname","eng_lname","vstatus","kayperson","value","wk","stg","is_cand","addr","con_yn","bhv","family_org","rel_1","rel_2","rmk" )

    def create(self, validated_data):
        return vinfo.objects.create(**validated_data)