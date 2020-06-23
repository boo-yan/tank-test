from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import time
import os
from selenium.webdriver.support.wait import WebDriverWait

# 需要安装的 apk 包(debug版)，放到当前目录
#debug_apk = os.path.join(os.path.dirname(__file__), "app-debug.apk")
desired_caps = {
    'platformName': "Android",
   # 'platformVersion': "8",
    'deviceName': "emulator-5554",
    'appPackage': "com.huyang.test",
    'appActivity': ".MainActivity",
    #'automationName': "UiAutomator2",
    # apk 包
    'app':"F://tank-wang//tank-test//app-release - 2020-06-23T160524.693.apk",
    'unicodeKeyboard': True,  # 使用unicodeKeyboard,即Appiuum自带键盘
    'resetKeyboard': True,  # 重新设置系统键盘为Appium自带键盘pip
    'noReset': True  # 每次启动不重置APP,即不执行清空APP数据操作
    # 'udid':"emulator-5554"

}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# driver.implicitly_wait(5) #隐式等待，5s里找到元素就开始执行 time.sleep(5)必须等待5s才开始执行
# WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.mymoney:id/next_btn'))
# 向左滑动4次，跳转引导页,调用swip方法，需要添加time.sleep(s)等待时间，否则会报错
# time.sleep(1)


def touch_tap(self, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
    '''
    method explain:点击坐标
    parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
    Usage:
        device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
    '''
    screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
    screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
    a = (float(x) / screen_width) * screen_width
    x1 = int(a)
    b = (float(y) / screen_height) * screen_height
    y1 = int(b)
    self.driver.tap([(x1, y1), (x1, y1)], duration)


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def swipLeft():
    l = get_size()
    x1 = int(l[0] * 0.9)
    x2 = int(l[1] * 0.2)
    y1 = int(l[0] * 0.5)
    driver.swipe(x1, y1, x2, y1, 1000)


def swipRight():
    R = get_size()
    x1 = int(R[0] * 0.2)
    x2 = int(R[1] * 0.9)
    y1 = int(R[0] * 0.5)
    driver.swipe(x1, y1, x2, y1, 1000)


def swipUp():
    U = get_size()
    y1 = int(U[0] * 0.8)
    y2 = int(U[1] * 0.2)
    x1 = int(U[0] * 0.2)
    driver.swipe(x1, y1, x1, y2, 1000)


def swipDown():
    U = get_size()
    y1 = int(U[0] * 0.2)
    y2 = int(U[1] * 0.8)
    x1 = int(U[0] * 0.2)
    driver.swipe(x1, y1, x1, y2, 1000)


# 根据类型、文本查找元素
def find_element_by_text(class_name, text):
    text_views = driver.find_elements_by_class_name(class_name)
    for text_view in text_views:
        if text_view.text == text:
            return text_view
    return None


# 等待 dom 生成后，再查找元素
def wait_element_by_class_name_and_text(class_name, text, timeout=10):
    driver.implicitly_wait(timeout)
    text_views = driver.find_elements_by_class_name(class_name)
    for text_view in text_views:
        if text_view.text == text:
            return text_view
    return None


# 等待并查找元素
def wait_element_by_class_name(class_name, timeout=10):
    driver.implicitly_wait(timeout)
    return driver.find_elements_by_class_name(class_name)


# 是不是第一次启动
first_init = wait_element_by_class_name_and_text("android.view.View", "引导图")
if first_init is not None:
    # 滑动app起始页，4页
    for i in range(4):
        # 调用左滑方法
        swipLeft()
        sleep(0.5)
    # 点击“立即开始”按钮
    driver.find_element_by_class_name("android.widget.Button").click()


# 进入登录界面
enter_login = wait_element_by_class_name_and_text("android.view.View", "云钱包请先登录云钱包")
if enter_login is not None:
    enter_login.click()
else:
    print("invalid login view")

# 登录
views = wait_element_by_class_name("android.widget.EditText")
if len(views) != 3:
    print("error get text input number")
else:
    account = views[0]
    password = views[1]
    verify_code = views[2]
    account.send_keys("13072374137")
    password.send_keys("123456aa")
    verify_code.send_keys("00")
# 查找登录按钮
login_btn = wait_element_by_class_name_and_text("android.widget.Button", "Log in")
if login_btn is not None:
    login_btn.click()
else:
    print("invalid login button")

sleep(30)
