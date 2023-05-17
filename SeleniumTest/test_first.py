import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.baidu.com")

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element(By.ID,"kw").send_keys("中华军事网")
        self.driver.find_element(By.ID, "su").click()
        self.driver.find_element(By.LINK_TEXT, '中华网')