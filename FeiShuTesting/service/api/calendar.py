# form __future__ import annotations
from pytestdemo.FeiShuTesting.service.api.event import Event
from pytestdemo.FeiShuTesting.service.api.feishu_api import FeiShuApi

class Calendar(FeiShuApi):

    def __init__(self,token,env = None,**kargs):
        super().__init__(token)
        self.calendar_id = kargs.get('calendar_id')
        self.color = kargs.get('color')
        self.description = kargs.get('description')
        self.permissions = kargs.get('permissions')
        self.role = kargs.get('role')
        self.summary = kargs.get('summary')
        self.type = kargs.get('type')
        self.summary_alias = kargs.get('summary_alias')
        # self.host = env
    def get_token(self):
        return self.token

    def create(self,summary,**kwargs):
        url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars'
        kwargs['summary'] = summary
        print(summary)
        j = self.request(
            url = url,
            method = 'post',
            json = kwargs
        )
        return j

    # @classmethod
    def list(self, page_size = 500, **kwargs)->list['Calendar']:
        url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars'
        j = self.request(
            url=url,
            method = 'get',
            params={'page_size':page_size,**kwargs}
        )
        calendar_list: list[Calendar]=[]
        for data in j['data']['calendar_list']:
            calendar_list.append(Calendar(token=self.token,**data))
        return calendar_list

    def delete(self,calendar_id = None,*args):
        if calendar_id is None:
            calendar_id = self.calendar_id
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars/:{calendar_id}'
        method = 'delete'
        self.request(
            url = url,
            method = method
        )
    def update(self,*args):
        pass

    @classmethod
    def get(cls,*args):
        pass

    def subscribe(self,*args):
        pass

    def unsubscribe(self,*args):
        pass

    # @classmethod
    def delete_all(self,*args):
        for c in self.list():
            c.delete()
        # calendar_ids = [c['calendar_id'] for c in j['data']['calendar.list']]
        # for id in calendar_ids:
        #     self.delete(id)

    def get_event(self):
        return list(Event())