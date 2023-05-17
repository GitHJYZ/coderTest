from pytestdemo.FeiShuTesting.service.api.calendar import Calendar
import pytest
from pytestdemo.FeiShuTesting.service.api.feishu import FeiShu
from time import sleep

feishu = FeiShu()
calendar=Calendar(feishu.get_token())
calendar.delete_all()
def test_list_no_calendar():
    calendars=calendar.list()
    # assert len(calendars['data']['calendar_list']) == 1
    assert len(calendars) == 1

def test_list_multi_calendar():
    Calendar.create("1")
    calendars=Calendar.list()
    assert len(calendars) == 2

    Calendar.create("2")
    calendars=Calendar.list()
    assert len(calendars) == 3
@pytest.mark.slow
def test_list_page_size():
    size = 30
    for i in range(size):
        sleep(0.2)
        calendar.create(f"batch_{i}")
    calendars=Calendar.list(page_size=size)
    assert len(calendars) == size

def test_list_mass_calendar():
    Calendar.delete_all()
    Calendar.create()
    calendars=Calendar.list()
    assert len(calendars) == 500

@pytest.mark.parametrize("page_size",[0,49,50,500,1000])
def test_list_mass_calendar(page_size):
    Calendar.create()
    calendars=Calendar.list(page_size)
    assert len(calendars) == page_size

def test_create():
    j=calendar.create(
        'ss-20',
        color=16711680,
        description='',
        permission='public'
    )
    assert j['code'] == 0
def test_delete():
    calendar_list = calendar.list()
    calendar_ids = [c.calendar_id for c in calendar_list if c.type != 'primary']
    for id in calendar_ids:
        calendar.delete(id)