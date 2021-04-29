#!/usr/local/bin/python
# Please visit http://selenium-python.readthedocs.org/en/latest/index.html for detailed installation and instructions

import unittest
import os
from selenium import webdriver

caps = {}
username = os.environ.get("LT_USERNAME")
key = os.environ.get("LT_ACCESS_KEY")
caps['name'] = os.environ.get("LT_BUILD_NAME")
caps['build'] = os.environ.get("LT_BUILD_NUMBER")
caps['browser_api_name'] = os.environ.get("LT_BROWSER")
caps['os_api_name'] = os.environ.get("LT_OPERATING_SYSTEM")
caps['screen_resolution'] = os.environ.get("LT_RESOLUTION")
caps['record_video'] = 'true'
print(username,key)
class SeleniumCBT(unittest.TestCase):
    def setUp(self):

        # start the remote browser on our server
        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (username, key)
        )

        self.driver.implicitly_wait(20)

    def test_CBT(self):

        # load the page url
        print('Loading Url')
        self.driver.get('http://crossbrowsertesting.github.io/selenium_example_page.html')

        # maximize the window - DESKTOPS ONLY
        # print('Maximizing window')
        # self.driver.maximize_window()

        # check the title
        print('Checking title')
        self.assertTrue("Selenium Test Example Page" in self.driver.title)

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
