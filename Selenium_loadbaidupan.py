#coding=utf-8
from selenium import webdriver
import os,time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
class loadbaidupan:

    #构造函数
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get("https://pan.baidu.com/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        self.driver = driver

    #析构函数
    def __del__(self):
        driver = self.driver
        driver.close()

    # 登陆
    def load(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='login-middle']/div/div[6]/div[2]/a").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(u"账户")#账号
        driver.find_element_by_name("password").send_keys(u"密码")#密码
        driver.find_element_by_id("TANGRAM__PSP_4__submit").click()
        time.sleep(3)

    #文件上传
    def fileup(self):
        driver = self.driver
        #driver.find_element_by_link_text(u"上传").click()
        driver.find_element_by_id("h5Input0").send_keys(r"C:\Users\nokia\PycharmProjects\output.txt")#要上传的文件地址
        time.sleep(1)

     #文件删除
    def filedete(self):
        driver = self.driver
        t = driver.find_element_by_link_text("output.txt")#要删除的文件
        ActionChains(driver).context_click(t).perform()
        time.sleep(1)
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"确定").click()
        time.sleep(3)

     #鼠标移动到头像
    def mousemove(self):
        driver = self.driver
        time.sleep(3)
        x1 = driver.find_element_by_xpath("//*[@id='dynamicLayout_0']/div/div/dl/dd[2]/span/span[1]/i")#这里确定鼠标移动位置的定位
        ActionChains(driver).drag_and_drop(x1, x1).perform()
        time.sleep(3)

    #鼠标移动后,点击个人资料
    def personalInfor(self):
        driver = self.driver
        driver.find_element_by_link_text(u"个人资料").click()
        time.sleep(3)

    #键盘输入需要查询的文件
    def searchfile(self):
        driver = self.driver
        driver.find_element_by_name("q").send_keys(u"文明6")#要搜索的文件
        driver.find_element_by_class_name("gHHsaL").click()
        time.sleep(3)

    #选中全部下载文件（文明6为例）
    def download(self):
        driver = self.driver
        driver.find_element_by_class_name("zbyDdwb").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"下载").click()
        time.sleep(4)
        try:
            driver.find_element_by_xpath("//*[@id='moduleDownloadDialog']/div[1]/div/span").click()
        except NoSuchElementException, e:
            assert 1 == 0


    def close(self):
        driver = self.driver
        driver.quit()





