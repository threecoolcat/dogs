from django.test import TestCase
from .views import aes_encode, aes_decode
import json
# Create your tests here.

# 测试类， 继承 TestCase
class TestFirst(TestCase):
    def setUp(self):
        pass

    # 测试方法， 以 test_ 开头
    # 测试加密解密方法
    def test_aes(self):
        key = '1111111111111111'
        text = 'to be aes'
        cipher = aes_encode(text, key)
        # print('cipher', cipher)
        data = aes_decode(cipher, key)
        # print('data', data)
        self.assertEqual(text, data, '加密解密失败')

    # 测试接口
    def test_GetMsg(self):
        response = self.client.get('/msg/')
        # 接口访问状态
        self.assertEqual(response.status_code, 200, '接口返回错误')
        text = response.content
        # 接口返回数据不为空
        self.assertIsNotNone(text, '数据为空')
        js = json.loads(text)
        # 接口数据可转换为json
        self.assertIsNotNone(js, '转换成json失败')