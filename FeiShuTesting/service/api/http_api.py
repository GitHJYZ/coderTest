import json
import requests as requests
from pytestdemo.FeiShuTesting.service.api.log import log


class HttpApi:
    def request(self, method, url, *args, **kwargs):
        input_data = {
            'url':url,
            'method':method,
            **kwargs
        }
        log.debug(json.dumps(input_data,indent=2,ensure_ascii=False))
        r = requests.request(
            method = method,
            url = url,
            **kwargs
        )
        log.debug(r.status_code)
        log.debug(json.dumps(r.json(),indent=2,ensure_ascii=False))
        return r.json()

