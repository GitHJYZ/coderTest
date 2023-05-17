import yaml
from selenium import webdriver


class BasePage:
    def __init__(self,base_driver = None):
        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            with open("data.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver

    def find(self, by, ele = None):
        """
        :param by:定位方式 css,xpath,id
        :param ele:元素定位
        :return
        """
        # 两种传入定位元素的方式，提高代码的兼容性
        if ele == None:
            return self.driver.find.element(*by)
        else:
            return self.driver.find.element(by, ele)