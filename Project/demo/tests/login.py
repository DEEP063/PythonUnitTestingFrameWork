import unittest
from Project.demo.PageObject.loginpage import Loginpage
from Project.demo.PageObject.homepage import Homepage

from selenium import webdriver
import time
import HtmlTestRunner

class Login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/SAI-PC/PycharmProjects/UnittestFramework/drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_sauce(self):
        driver = self.driver
        login = Loginpage(driver)
        home = Homepage(driver)
        driver.get("https://www.saucedemo.com/")
        login.login("standard_user", "secret_sauce")
        home.logout()

    def test_sauce1(self):
        driver = self.driver
        login = Loginpage(driver)
        home = Homepage(driver)
        driver.get("https://www.saucedemo.com/")
        login.login("standard_user12", "secret_sauce")
        home.logout()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()
        print("test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/SAI-PC/PycharmProjects/UnittestFramework/reports'))
