from django.test import TestCase
from django.http import HttpRequest, request, response
from posnegDiscriminatorApp.views import top

# Create your tests here.

'''
トップページのステータスコードとレスポンスをテストする単純なコード
class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(response.status_code, 200)
    
    def test_top_returns_expected_content(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(response.content, b"Hello World!")
'''
# ↑のテストケースに、URLディスパッチャのルーティングが
# 正しく動作しているかテストするのが以下
class TopPageRoutingTest(TestCase):
    def test_top_returns_200(self):
        '''
        Clientクラスのオブジェクトclientを用いることで、
        任意のエンドポイントに対してGETやPOSTを送った際の
        挙動が確認できる
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_top_returns_expected_content(self):
        response = self.client.get('/')
        self.assertEqual(response.content, b'Hello World!')