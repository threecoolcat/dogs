from rest_framework import serializers

class PurchaseMSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # 采购单号，自动生成
    title =serializers.CharField(max_length=60)  # 采购单名称
    buyer =serializers.CharField(max_length=12)  # 采购员
    supplier =serializers.CharField(max_length=60)  # 供货商
    call = serializers.CharField(max_length=20)  # 联系电话
    time = serializers.DateTimeField()  # 采购时间

class MsgSerializer(serializers.Serializer):
    author=serializers.CharField(max_length=20,required=True,label='信息发送人员')
    title=serializers.CharField(max_length=40,required=True,label='信息发送题目')
    content= serializers.CharField(max_length=100, required=True, label='信息发送内容')

from first.models import PurchaseM,PurchaseDetail  #导入需要序列化的模型
class PurchaseMModelSerial(serializers.ModelSerializer):
    class Meta:
        model=PurchaseM   #设置需要序列化的模型
        fields='__all__'       #对模型所有字段进行序列化
        extra_kwargs = {
                        'title': {'write_only': False},
                        'buyer': {'write_only': False},
                        'supplier': {'write_only': False},
                        'call': {'write_only': False},
                        'time': {'write_only': False},   }
        #exclude=['id']        #排除id字段

from first.models import PurchaseM,PurchaseDetail  #导入需要序列化的模型
class PurchaseMDModelSerial(serializers.ModelSerializer):
    class Meta:
        model=PurchaseDetail  #设置需要序列化的模型
        fields='__all__'       #对模型所有字段进行序列化

from first.models import PurchaseM #导入需要序列化的模型
class PurchaseMDModelSerialDB(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # 采购单号，自动生成
    title = serializers.CharField(max_length=60)  # 采购单名称
    buyer = serializers.CharField(max_length=12)  # 采购员
    supplier = serializers.CharField(max_length=60)  # 供货商
    call = serializers.CharField(max_length=20)  # 联系电话
    time = serializers.DateTimeField()  # 采购时间
    def create(self, validated_data):            #不传递实例时，新建数据库记录
        """新建"""
        return PurchaseM.objects.create(**validated_data)

    def update(self, instance, validated_data):    #传递实例时，更新实例对象的数据
        """更新，instance为要更新的对象实例"""
        instance.title = validated_data.get('title', instance.title)
        instance.buyer= validated_data.get('buyer', instance.buyer)
        instance.supplier=validated_data.get('supplier', instance.supplier)
        instance.call = validated_data.get('call', instance.call)
        instance.time= validated_data.get('time', instance.time)
        instance.save()
        return instance

class PDMSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetail       # 与PurchaseDetail表对应
        fields = "__all__"
        depth = 1