from django.contrib import admin
from first.models import PurchaseM,PurchaseDetail
class PurchaseMAdmin(admin.ModelAdmin):
    list_display =['title','buyer','supplier','call','time']

admin.site.register(PurchaseM,PurchaseMAdmin)  #注册主表
class PurchaseDAdmin(admin.ModelAdmin):
    list_display =('name','number','unit','price','Mid_id')

admin.site.register(PurchaseDetail,PurchaseDAdmin) #注册明细表
admin.site.site_header = '三酷猫后台管理系统'
admin.site.site_title = '水果后台'