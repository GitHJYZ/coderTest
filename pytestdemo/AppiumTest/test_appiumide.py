from appium import webdriver
from selenium.webdriver.common.by import By
desire_cap = {
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".common.MainActivity",
  "noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
driver.implicitly_wait(10)
el1 = driver.find_element(By.ID,"com.xueqiu.android:id/search_input_text")
el1.click()
el1.send_keys("alibaba")
el2 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el2.click()
