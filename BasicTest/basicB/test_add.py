from Calculator import Calculator
import pytest
import yaml


def get_datas():
    with open("../datas/calc.yaml") as f:
        datas = yaml.safe_load(f)
    return datas

#install pip yaml
"""
def test_getdatas():
    with open("./datas/calc.yaml") as f:
        datas = yaml.safe_load(f)
    print(datas)
"""
@pytest.fixture(scope='class')
def initcalc_class():
    #setup
    print("setup")
    calc = Calculator()
    yield calc
    #teardown
    print("teardown")

@pytest.fixture(params=get_datas()['int_datas'],ids=get_datas()['ids'])
def get_datas_calc(request):
    return request.param
def test_get_datas(get_datas_calc):
    print(get_datas_calc)

class TestCal:
    # def setup_class(self):
    #     print("setup")
    #     self.calc= Calculator()
    # def teardown_class(self):
    #     print("teardown")

    # @pytest.mark.parametrize('a,b,expect', get_datas()['int_datas'], ids=get_datas()['ids'])
    def test_add_int(self,initcalc_class,get_datas_calc):
        assert get_datas_calc[2] == initcalc_class.add(get_datas_calc[0], get_datas_calc[1])

    @pytest.mark.parametrize('a,b,expect', [
        [1.0, 0, 1.0], [1.0, 10, 11.0], [21.0, 0, 21.0], [11.1, 0, 11.1]
    ], ids=['浮点数1', '浮点数2', '浮点数3', '浮点数4'])
    def test_add_float(self,initcalc_class, a, b, expect):
        assert expect == round(initcalc_class.add(a, b),2)

    @pytest.mark.parametrize('a,b,expect', [
        [1, 0, False], [1, 10, 0.1], [21, 0, False], [0, 11, 0]
    ], ids=['d1', 'd2', 'd2', 'd4'])
    def test_div(self, initcalc_class,a, b, expect):
        try:
            assert expect == initcalc_class.div(a, b)
        except ZeroDivisionError:
            print("除数为零")

