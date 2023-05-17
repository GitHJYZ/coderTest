
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import time
class TestDemo:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "su").click()
        ele = self.driver.find_element(By.LINK_TEXT, '霍格沃兹测试学院-软件自动化测试开发培训_接口性能测试')
        assert ele

class TestWework:
    def test_Wework(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9227"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID,"menu_contacts").click()
        cookie = self.driver.get_cookies()
        with open("test_web_wechat/testcase/data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie,f)

def test_cookie():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688855251370548'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970326352985012'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688855251370548'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '03526377'}, {'domain': '.work.weixin.qq.com', 'expiry': 1679923123, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'NaY6QsGDGUohwZMs5aEvrUbVILMgCUvR9jMuGnCWl2vD2N9IfOCqr-uxtKnvP4_Y'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '4588960660'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1650543134, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '0001000047f02588244ef66b77189f01b9db892a4e151d9e3746b08c03a7c2c12893b91b56f48309bd5d4298'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'b3Xo6qo0UT'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'kCaK3dfQM4lRLx5_J7aL0w3mKzsD3a21-NZPeani12twQ2V-ciYaj9jHMnDWv0f-5Kx-WY0fjDsHefC-s5Dt2byI3Ao2Ts9F7f0tgYSG8Smw15TRageRS6AVjbumCJ3Rd4yiD58DhTJmFtC3CFcuX2WBv58bdlgsNJNTMvVUP581EYhqZvhweH-nSl08QGyxElajY1fsmHCeMWQSQSl4DOPJKOG18-lBkQi8Tu5X0wwgcI_IsTBJqK2vuQ1Va_6l4lcOsM12oP_pZGYvjTzp4A'}, {'domain': '.qq.com', 'expiry': 1650543134, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o1792889813'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1656244'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '089f95a64ad52621c4fea1ee18498b837f2c2f8c354381ec404626024c6afa8e'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650985147, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    time.sleep(5)

def test_cookie_v2():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    with open("test_web_wechat/testcase/data.yaml", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")