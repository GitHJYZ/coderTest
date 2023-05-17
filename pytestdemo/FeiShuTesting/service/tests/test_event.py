from calendar import Calendar
from pytestdemo.FeiShuTesting.service.api.feishu import FeiShu

feishu = FeiShu()
calendar_default = Calendar(feishu.get_token())
calendar_default.delete_all()
calendar = calendar_default.create('ck888')

def test_list():
    calendar.get_event()