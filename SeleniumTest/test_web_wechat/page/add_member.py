from time import sleep
from pytestdemo.SeleniumTest.test_web_wechat.page.base_page import BasePage
from pytestdemo.SeleniumTest.test_web_wechat.page.contact import ContactPage
from selenium.webdriver.common.by import By

class AddMemberPage(BasePage):
    # 设定元组
    ele_username = (By.ID, "username")
    ele_accid = (By.ID, "memberAdd_acctid")
    ele_phone = (By.ID, "memberAdd_phone")
    def add_member(self,name,accid,phone):
        #*的作用是解元组
        self.driver.find_element(*self.ele_username).send_keys(name)
        self.driver.find_element(*self.ele_accid).send_keys(accid)
        self.driver.find_element(*self.ele_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(3)
        # 页面的return 分成两个部分
        # 1.其他页面的实例
        # 2.用例所需的断言
        # 3.快捷import alt + enter
        return ContactPage(self.driver)

    def add_member_fail(self,name,accid,phone):
        self.driver.find_element(*self.ele_username).send_keys(name)
        self.driver.find_element(*self.ele_accid).send_keys(accid)
        self.driver.find_element(*self.ele_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ww_inputWithTips_tips").click()
        error_list = []
        for ele in element:
            error_list.append(ele.text)
        return error_list
