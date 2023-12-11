# ---encoding:utf-8---
# @Time    : 2023/12/11 16:16
# @Author  : 辉
# @Email   ：XXXXXX@qq.com
# @File    : ByteDance.py
# @Project : myByteDanceTest
# @Software: PyCharm
import time
from pynput.keyboard import Controller, Key
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# 调用键盘输入
def systemInput(inputValue):
    # 清空输入框内容
    Controller().press(Key.delete)
    # 键入剪切板内容
    Controller().type(inputValue)
    # 点击回车键
    Controller().press(Key.enter)


# 显示等待封装
def findElement(driver, by, ele):
    try:
        res = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(locator=(by, ele)))
        time.sleep(1)
        return res
    except Exception:
        pass


option = webdriver.ChromeOptions()
option.add_argument('--start-maximized')
driver = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(),
    options=option
)
# 进入官网
driver.get('https://www.feishu.cn/')
# 点击关闭弹窗
findElement(driver, By.XPATH, '//*[@data-elem-id="IFnHep2Rb0"]').click()
# 点击登录按钮
findElement(driver, By.XPATH, '//*[text()="登录"]').click()
# 点击切换到账号密码输入
findElement(driver, By.CLASS_NAME, 'switch-login-mode-box').click()
# 输入账号
findElement(driver, By.CLASS_NAME, 'mobile-input-phone').send_keys('17706914195')
# 点击我已阅读
findElement(driver, By.CLASS_NAME, 'ud__checkbox__input').click()
# 点击下一步
findElement(driver, By.XPATH, '//button[@data-test="login-phone-next-btn"]').click()
time.sleep(5)
# 密码框
findElement(driver, By.XPATH, '//*[@placeholder="请输入密码"]').send_keys('XXXXXX')
# 点击下一步
findElement(driver, By.XPATH, '//button[@data-test="login-pwd-next-btn"]').click()

# 点击拓展功能按钮
findElement(driver, By.XPATH, '//*[@data-icon="DialpadOutlined"]').click()
# 点击消息按钮
findElement(driver, By.XPATH, '//*[@title="消息"]').click()
# 切换到飞书消息页
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    if driver.title == "消息 - 飞书":
        # 如果是目标窗口，退出循环
        break

# 点击联系人
findElement(driver, By.XPATH, '//*[@data-tip="tip-contacts"]').click()
# 点击tester2
findElement(driver, By.XPATH, '//*[text() = "tester2"]').click()
# 点击发送消息
findElement(driver, By.CLASS_NAME, 'larkc-usercard__cta-button').click()

# 点击发送消息框
ele = findElement(driver, By.CLASS_NAME, 'lark-editor-container')
ActionChains(driver).move_to_element(ele).click()

# # 发送消息
systemInput('1234567890')
time.sleep(3)
driver.quit()
