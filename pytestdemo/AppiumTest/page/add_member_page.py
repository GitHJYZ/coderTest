from appium.webdriver.common.mobileby import MobileBy
from pytestdemo.AppiumTest.page.base_page import BPage

class AddMemberPage(BPage):
    def addmember_bymenual(self):
        # click 手动输入id
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from pytestdemo.AppiumTest.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def find_toast(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        #return True