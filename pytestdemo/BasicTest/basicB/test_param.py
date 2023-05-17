import pytest

"""
@pytest.mark.parametrize('key,result',[
    ['appium',100],['selenium',200],['requests',200],['docker',300]
],ids=['a','b','c','d'])

def test_interface(key,result):
    url = f"http://ceshiren.com/key={key}"
    print(url,result)
"""

#卡迪尔积
@pytest.mark.parametrize('a',[1,2,3])
@pytest.mark.parametrize('b',['int','string','float'])
def test_ab(a,b):
    print(a,b)