from pytestdemo.service.base_api import BaseApi

class WeWork(BaseApi):
    def __init__(self,corpid,secret):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            'method':'get',
            'params':{
                "corpid": corpid,
                "corpsecret": secret
            }
        }
        r = self.request(data)
        self.access_token = r.json()['access_token']


