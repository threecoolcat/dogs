from django.db import models

# Create your models here.
class PurchaseM(models.Model):
    id=models.AutoField(primary_key=True)    #采购单号，自动生成
    title=models.CharField(max_length=60)    #采购单名称
    buyer=models.CharField(max_length=12)    #采购员
    supplier=models.CharField(max_length=60) #供货商
    call=models.CharField(max_length=20)     #联系电话
    time=models.DateTimeField()              #采购时间
    def __str__(self):
        return self.supplier+str(self.time)
    class Meta:
        verbose_name = '采购主表'
        verbose_name_plural = '采购主表'  # 优先显示，去掉”s“

class PurchaseDetail(models.Model):
    id=models.AutoField(primary_key=True)    #入单顺序号，自动生成
    name=models.CharField(max_length=60)    #采购水果名称
    number=models.FloatField()              #采购数量
    unit=models.CharField(max_length=6)     #采购单价
    price=models.DecimalField(max_digits=10,decimal_places=3) #采购单价
    Mid=models.ForeignKey(PurchaseM,on_delete=models.Case) #关联主表的id
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '采购明细表'  # 优先显示，去掉”s“