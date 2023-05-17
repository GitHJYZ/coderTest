from pytestdemo.SeleniumTest.test_web_wechat.page.base_page import BasePage
from selenium.webdriver.common.by import By
class ContactPage(BasePage):
    def get_contact_list(self):
        ele_list = self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        print(ele_list)
        name_list = []
        for ele in ele_list:
            name_list.append(ele.text)
        print(name_list)
        return name_list