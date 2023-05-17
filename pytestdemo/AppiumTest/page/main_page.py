#主页面
from appium.webdriver.common.mobileby import MobileBy
from pytestdemo.AppiumTest.page.base_page import BPage
from pytestdemo.AppiumTest.page.contactlist_page import ContactListPage

class MainPage(BPage):

    def goto_contactlist(self):
        # click 通讯录
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        #self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        return ContactListPage(self.driver)