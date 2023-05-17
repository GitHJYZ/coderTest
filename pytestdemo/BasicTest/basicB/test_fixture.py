import pytest

# @pytest.fixture(autouse=True)
# @pytest.fixture(scope = "module")
# def a():
#     print("测试auto")
#
# @pytest.fixture()
# def connectDb():
#     print("链接数据库")
#     # return "database datas"
#     yield "搜索结果" #返回后面的结果
#     #相当于 teardown 操作 yeild 相当于 return
#     print("断开数据库")
#
# @pytest.fixture()
# def login():
#     print("open")
#     username = "hogwarts"
#     password = "123"
#     return username,password

def test_search(connectDb):
    print("搜索")

# @pytest.mark.usefixures('logon')
def test_add_cart():
    print("添加购物车")

def test_order(login,connectDb):
    print(login)
    print("订单")