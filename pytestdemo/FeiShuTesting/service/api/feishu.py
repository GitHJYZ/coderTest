from pytestdemo.FeiShuTesting.service.api.http_api import HttpApi


class FeiShu(HttpApi):
    token: str = None
    def __init__(self, app_id = 'cli_a2d03661f4b8900c', app_secret = 'KimCZW3Jg3JghaeZJ6SGWfuIdLOWClf3'):
        self.token: str = None
        self.app_id = app_id
        self.app_secret = app_secret

    def get_token(self):
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
        if self.token is None:
            return self.token
        else:
            j =self.request(
                url = url,
                method='post',
                json={
                    'app_id':self.app_id,
                    'app_secret':self.app_secret
                }
            )
            self.token = j['tenant_access_token']
        return self.token