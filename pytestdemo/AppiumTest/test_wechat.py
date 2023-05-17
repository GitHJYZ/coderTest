
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
import pytest

class TestCh:
  def setup_class(self):
    self.faker = Faker('zh-CN')
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

  def setup(self):
  # 初始化
    self.driver.launch_app()
  def teardown(self):
    #关闭
    self.driver.close_app()

  def teardown_class(self):
    # 资源销毁
    self.driver.quit()

  def test_dake(self):
    #测试用例
    self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
    #uiautonmator的定位方式，android原生定位方式，滚动查找某个文字
    self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector()'
                             '.scrollable(true).instance(0)).'
                             'scrollIntoView(new UiSelector().'
                             'text("打卡").instance(0));').click()
    #self.driver.update_settings({'waitForIdleTimeout':0})
    self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
    self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
    self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']").click()

  def swipe_find(self,text,num = 3):
    # 默认查找3次
    self.driver.implicitly_wait(1)
    for i in range(0,num):
        try:
            element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
            self.driver.implicitly_wait(5)
            return element
        except NoSuchElementException:
          print("未找到，滑动")

          size = self.driver.get_window_size()
          #width height
          width = size['width']
          height = size['height']

          start_x = width/2
          start_y = height*0.8
          end_x = start_x
          end_y = height*0.3

          duration = 2000 #ms
          self.driver.swipe(start_x,start_y,end_x,end_y,duration)
        if i == num-1:
          self.driver.implicitly_wait(5)
          raise NoSuchElementException(f"找了{i}次，未找到")

  @pytest.mark.parametrize('a',['aa','bb'])
  def test_addcontact(self,a):

    name = self.faker.name()
    phonenum = self.faker.phone_number()

    self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
    self.swipe_find('添加成员').click()
    self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
    self.driver.find_element(MobileBy.XPATH,
                             "//*[contains(@text,'姓名')]/../"
                             "android.widget.EditText ").send_keys(name)
    self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(phonenum)
    self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
    self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")