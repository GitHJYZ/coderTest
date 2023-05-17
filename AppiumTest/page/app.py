#app.py app相关，启动，关闭。重启
from appium import webdriver
from pytestdemo.AppiumTest.page.main_page import MainPage
from pytestdemo.AppiumTest.page.base_page import BPage


class App(BPage):

    def start(self):
        if self.driver == None:
            print("driver 未初始化")
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "mumux"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            # 客户端和服务端链接
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 每次调用find_element时都会激活这种等待方式
            self.driver.implicitly_wait(5)
        else:
            #复用driver
            print("复用driver ")
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        pass

    def goto_main(self):
        return MainPage(self.driver)