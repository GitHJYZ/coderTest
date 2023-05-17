import pytest
from Calculator import Calculator

@pytest.fixture()
def connectDb():
    print("链接数据库")
    # return "database datas"
    yield "搜索结果" #返回后面的结果
    #相当于 teardown 操作 yeild 相当于 return
    print("断开数据库")

@pytest.fixture()
def login():
    print("open")
    username = "hogwarts"
    password = "123"
    return username,password

@pytest.fixture(scope='class')
def initcalc_class():
    #setup
    print("setup")
    calc = Calculator()
    yield calc
    #teardown
    print("teardown")

@pytest.fixture(params=[[0.1,0,False],[2, 2, 2]],ids=['f1', 'f2'])
def get_div_datas(request):
    return request.param

def pytest_collection_modifyitems(session, config, items:list):
    print("这里搜集所有测试用例")
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'foo' in item.name:
            item.add_marker(pytest.mark.foo)
        elif 'last' in item.name:
            item.add_marker(pytest.mark.last)
