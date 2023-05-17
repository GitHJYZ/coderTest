from pytestdemo.AppiumTest.page.base_page import BPage
from pytestdemo.AppiumTest.page.add_member_page import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy
class EditMemberPage(BPage):

    def edit_member(self,name,phonenum):
        # input name
        # input phonenum
        # 保存
        print(name)
        print(phonenum)
        self.find(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../"
                                 "android.widget.EditText ").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        return AddMemberPage(self.driver)