from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from first.models import PurchaseM,PurchaseDetail  #导入需要序列化的模型
from first.Serial import PurchaseMSerializer,MsgSerializer
from rest_framework.renderers import JSONRenderer  #JSON格式渲染
from django.http import HttpResponse               #返回响应结果
def GetPurchaseM(request):
    if request.method=="GET":
        purchaseM=PurchaseM.objects.get(id=1)     #从模型获取一条记录
        serial=PurchaseMSerializer(instance=purchaseM,many=False) #序列化模型实例
        print(serial.data) #把序列化后的数据输出到命令提示符里
        json=JSONRenderer().render(serial.data)   #把序列化数据渲染成JSON格式
        return HttpResponse(json, content_type='application/json')

from datetime import datetime
class Message(object):                  #假设三酷猫需要跟公司内部人员的沟通消息
    def __init__(self,author,title, content,Buildtime=None):
        self.author=author             #发送信息人员
        self.title = title             #信息题目
        self.content = content         #信息内容
        self.Buildtime = Buildtime or datetime.now() #信息记录时间
msg1=Message(author='三酷猫',title='采购水果任务', content='采购1000斤海南椰子')
msg2=Message(author='三酷猫',title='采购水果任务', content='采购1000斤新疆苹果')
msg=[msg1,msg2]

def GetMsg(request):
    if request.method == "GET":
        Msg=MsgSerializer(instance=msg,many=True)  #序列化消息类实例
        print(Msg.data)
        msgs=JSONRenderer().render(Msg.data)   #把序列化数据渲染成JSON格式
        return HttpResponse(msgs, content_type='application/json')

from first.Serial import PurchaseMModelSerial,PurchaseMDModelSerial
from rest_framework.views import APIView
class PurchaseMV(APIView):               #APIView的基本使用方法和View类似
    def get(self, request):
        MM=PurchaseM.objects.all()       #获取模型对象数据
        for one in MM:
            print(one)
        Sdetail=PurchaseMModelSerial(instance=MM,many=True) #模型数据序列化
        return Response(Sdetail.data)

from rest_framework.parsers import JSONParser
from io import BytesIO
def ShowDModelSerial(request):
    if request.method=='GET':
        Detail=PurchaseDetail.objects.filter(id__gte=1)  #获取id>=1的记录
        detail=PurchaseMDModelSerial(instance=Detail,many=True)
        sdata= JSONRenderer().render(detail.data)  # 把序列化数据渲染成JSON格式
        print('输出JSON数据：')
        print(sdata)   #序列化并渲染后的数据
        data=JSONParser().parse(BytesIO(sdata))
        print('输出python原生数据：')
        print(data)    #反序列化后的数据
        return HttpResponse(sdata, content_type='application/json')

from rest_framework.response import Response
from first.Serial import PurchaseMDModelSerialDB
def TestPMDB(request):                         #模拟从客户端以POST方式获取需提供的数据
    data={'id':10,'title':'干果采购单','buyer':'三酷猫','supplier':'TOM','call':'88888888','time':datetime.now()}
    dbData = PurchaseM.objects.filter(id=data['id'])  # 获取数据对象
    DBS = PurchaseMDModelSerialDB(data=data)  # 没有为instance参数提供模型数据
    if DBS.is_valid():  # 验证数据
        if dbData:  # 有记录，则修改记录
            DBS.update(instance=dbData, validated_data=data)
        else:
            DBS.save()  # 自动调用create()方法
        return HttpResponse(data)
    else:
        if dbData:  # 有记录，则修改记录
            DBS.update(instance=dbData, validated_data=data)
        else:
            DBS.save()  # 自动调用create()方法
        return HttpResponse(data)
    return HttpResponse(DBS.errors, status=404)  # 验证失败，给出出错信息

class PurchaseDM(APIView):               #APIView的基本使用方法和View类似
    def get(self, request):              #GET方法获取数据
        MM=PurchaseM.objects.all()       #获取模型对象数据
        Sdetail=PurchaseMModelSerial(instance=MM,many=True) #模型数据序列化
        return Response(Sdetail.data)
    def post(self,request):             #POST方法从客户端获取数据，并验证保存数据
        id=request.data.get(id=10)
        dbData=PurchaseM.objects.filter(id=id).first()
        sdata=PurchaseMModelSerial(data=dbData)
        if sdata.is_valid():
            if dbData :                  #存在数据库记录，更新记录
                sdata.update(instance=dbData,data=request.data)
            else:
                sdata.save()             #不存在，则新建记录
            return HttpResponse(request.data)
        return HttpResponse(sdata.errors, status=404)  # 验证失败，给出出错信息

from first.Serial import PDMSerializer
from first.models import PurchaseDetail
class PDM(APIView):                       #APIView的基本使用方法和View类似
    def get(self, request):              #GET方法获取数据
        MM=PurchaseDetail.objects.all()       #获取模型对象数据
        Sdetail=PDMSerializer(instance=MM,many=True) #模型数据序列化
        return Response(Sdetail.data)
