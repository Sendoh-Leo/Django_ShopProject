#coding:utf-8
#date:2020/5/822:46
#author:CQ_Liu
import json
from random import random
import string
import requests


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code,mobile):
    # 需要传递的参数
        parmas = { "apikey": self.api_key,
                   "mobile": mobile,
                   "text": "【刘承乾test】您的验证码是{code}。如非本人操作，请忽略本短 信".format(code=code)
                   }
    # 向API发送post请求
        response = requests.post(self.single_send_url, data=parmas)
    # 获取响应数据, 默认响应的信息时json字符串。 {'code':0, 'msg': '发送成功'}
        re_dict = json.loads(response.text)
        return re_dict

    @staticmethod
    def generate_code(count=6):
        """生成指定长度验证码"""
        return "".join(random.sample(string.digits, count))

if __name__ == '__main__':
    # 例如：9b11127a9701975c734b8aee81ee3526
    #API-KEY值是注册yunpina时生成的api-key
    API_KEY = "xxxxxx"
    yun_pian = YunPian(api_key=API_KEY)
    #生成验证码
    code = yun_pian.generate_code()
    #发送验证短信，手机号码为真实的手机号码
    result = yun_pian.send_sms(code, "手机号码")
    print(result)