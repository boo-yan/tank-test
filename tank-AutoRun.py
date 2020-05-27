# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import time
import os

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
    'platformName':"Android",
    'deviceName':"emulator-5554",
    'appPackage':"com.lihao.app",
    'appActivity': ".MainActivity",
    #'app':"D:\\aPackage\\app-debug.apk",
    'unicodeKeyboard':True,  #使用unicodeKeyboard,即Appiuum自带键盘
    'resetKeyboard':True,# 重新设置系统键盘为Appium自带键盘pip
    'noReset':True #每次启动不重置APP,即不执行清空APP数据操作
   # 'udid':"emulator-5554"

}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
#driver.implicitly_wait(5) #隐式等待，5s里找到元素就开始执行 time.sleep(5)必须等待5s才开始执行




#重写元素定位的方法
class Action (object):
    def __init__(self, se_driver):
        self.driver = se_driver
#
    def findId(self,id):
        try:
            f=self.driver.find_elment_by_id(id)
            return f
        except Exception as e:
            print("未找到%s"%(id))
#通过xpath定位
    def findXpath(self,xpath):
        try:
            f=self.driver.find_elment_by_xpath(xpath)
            return f
        except Exception as e:
            print("未找到%s"%(xpath))



#WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.mymoney:id/next_btn'))
#向左滑动4次，跳转引导页,调用swip方法，需要添加time.sleep(s)等待时间，否则会报错
time.sleep(1)

for i in range(4):
    swipLeft()
    sleep(0.5)
#点击“立即开始”
TouchAction(driver).tap(x=528, y=1616).perform()
my=driver.find_element_by_xpath()
