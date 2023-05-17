from pytestdemo.FeiShuTesting.service.api.http_api import HttpApi


class FeiShuApi(HttpApi):
    def __init__(self,token):
        self.token = token

    def get_token(self):
        pass
    def request(self,method,url,*args,**kwargs):
        if 'headers' in kwargs:
            kwargs['headers']['Authorization'] = f'Bearer {self.token}'
        else:
            kwargs['headers'] = {'Authorization' : f'Bearer {self.token}'}

        #todo: 多环境支持
        #url.replace('host',self.env)
        #kwargs['headers']['HOST']= host

        j = super().request(
            method = method,
            url = url,
            **kwargs
        )
        return j

