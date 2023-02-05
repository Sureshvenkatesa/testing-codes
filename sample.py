import datetime
import traceback
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from utilities import xlutils

# from webdriver_manager.chrome import ChromeDriverManager
import shutil
import os

n = 0


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.chrome("C:\\Users\\Smart\\Downloads\\chromedriver_win32\\chromedriver.exe")

    def login(self):

        self.driver.get("https://netbanking.kotak.com/knb2/")
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("567947611")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Captcha']").click()
        time.sleep(20)

        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@id='credentialInputField']").send_keys("Imperia@1234")
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Secure login']").click()
        time.sleep(40)
        try:
            self.driver.find_element(By.XPATH,"//div[@class='accounts-more-data position-relative cursor-pointer ng-star-inserted']//span[@class='marL04 padB01 padT01 paddLeft20']").click()
            time.sleep(10)
            iframe = self.driver.find_element(By.XPATH, "//iframe[@id='knb2ContainerFrame']")
            self.driver.switch_to.frame(iframe)
            time.sleep(5)
        except:
            self.login()

    def test_a_login(self):

        global n
        while n <= 30:
            n = n + 1
            try:
                # flag1= self.driver.find_element(By.XPATH,"//div[@class='accounts-more-data position-relative cursor-pointer ng-star-inserted']")
                # self.driver.execute_script("arguments[0].scrollIntoView();",flag1)
                # time.sleep(8)
                # self.driver.find_element(By.XPATH,"//div[@class='accounts-more-data position-relative cursor-pointer ng-star-inserted']").click()
                # time.sleep(10)

                # flag = self.driver.find_element(By.XPATH, "")
                # self.driver.execute_script("arguments[0].scrollIntoView();",flag)
                # time.sleep(8)

                self.driver.find_element(By.XPATH, "//a[normalize-space()='Last month']").click()
                time.sleep(8)
                self.driver.find_element(By.XPATH, "//a[@id='selectButton2']").click()
                time.sleep(5)
                self.driver.find_element(By.XPATH, "//a[@id='sarea2a1']").click()
                time.sleep(5)
                self.driver.find_element(By.XPATH, "//input[@id='downloadRpt']").click()
                time.sleep(8)


            except:
                self.login()

