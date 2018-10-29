import unittest
from selenium import webdriver
import requests
import json
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time 

class BroserStackTest(unittest.TestCase):
    def setUp(self):
        self.test_result = None
        desired_cap = {
        'platform' : 'WIN10',
        # 'platform' : 'any',

        'browserName' : 'chrome',
        'version' : '67.0',
        'name' : 'Log Test',
        "build_name": "Real test build 15",
        # "selenium_version": "3.7.0",

        }
        url = "https://dev-ml.lambdatest.com/wd/hub"
        # url = "http://localhost:4449/wd/hub"


        self.driver = webdriver.Remote(
            desired_capabilities=desired_cap,
            command_executor= url
        )

        self.driver.implicitly_wait(2)

    def test_CBT(self):
            self.driver.get('https://accounts.lambdatest.com')
            username = self.driver.find_element_by_name("email")
            username.send_keys("nikhily@lambdatest.com")
            password=self.driver.find_element_by_name("password")
            password.send_keys("111111")
            loginbutton=self.driver.find_elements_by_xpath("//*[contains(text(), 'LOGIN')]")
            loginbutton[0].click()

            # time.sleep(40)
            self.driver.save_screenshot("screenshot.png")
            self.test_result = 'pass'
            self.driver.quit()
       

if __name__ == '__main__':
    unittest.main()
