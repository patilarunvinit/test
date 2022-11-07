
from django.contrib import admin
from .models import vinfo
# Register your models here.
class infoAdmin(admin.ModelAdmin):
    list_display = ("vno","area","ward","mr_fname","mr_mname","mr_lname","eng_fname","eng_mname","eng_lname","vstatus","kayperson","value","wk","stg","is_cand","addr","con_yn","bhv","family_org","rel_1","rel_2","rmk" )
admin.site.register(vinfo,infoAdmin)