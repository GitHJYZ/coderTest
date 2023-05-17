from pytestdemo.server_apiObject.base_api import BaseApi

class Wework(BaseApi):
    def __init__(self, secret):
        corpid = 'ww9a7c9f39d084b5a1'
        # corpsecret = 'i8lbbMoby8YP1nJoDJuhT8Xc52-PRfB-vrjSTDcs1YM'
        # XH_5yu4cp94O_NuSC_iQA7sbHwtHTBMxi-6A6tWBAZs
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "method": "get",
            "params": {
                'corpid': corpid,
                'corpsecret': secret
            }
        }
        r = self.request(data)
        self.access_token = r.json()["access_token"]