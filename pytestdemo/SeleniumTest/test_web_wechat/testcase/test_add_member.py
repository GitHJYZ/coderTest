import pytest

from pytestdemo.SeleniumTest.test_web_wechat.page.main_page import MainPage

class TestAddMember():

    def setup_class(self):
        self.main_page = MainPage()

    @pytest.mark.parametrize("username,accid,phone",[("yingcha","59624","18126548316")])
    def test_add_member(self,username,accid,phone):
        main_page = MainPage()
        # add_member = AddMemberPage()
        name_list = self.main_page.goto_add_member().add_member(username,accid,phone).get_contact_list()
        assert username in name_list
        # add_member.add_member()

    @pytest.mark.parametrize("username,accid,phone", [("jingchu", "54625", "18826548316")])
    def test_add_member_fail(self,username,accid,phone):
        data_list = self.main_page.goto_add_member().add_member_fail(username,accid,phone)
        err = [i for i in data_list if i != ""]
        assert "jingchu" in err[0]