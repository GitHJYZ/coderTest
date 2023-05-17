import requests

class BaseApi():
    def request(self,request: dict):
        #多协议兼容
        if "url" in request:
            return self.http_request(request)
        if 'rcp' == request.get("protocol"):
            return self.rcp_request(request)

    def http_request(self,request):
        return requests.request(**request)

