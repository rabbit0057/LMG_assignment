import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from driver.config_driver import Driver
import HtmlTestRunner

from driver.desiredcapabilities import *

from pages.app_reset_start_time import app_reset_start_time
from pages.app_battery_metrics import app_battery_metrics
from pages.app_memory_metrics import app_memory_metrics
from pages.app_permission import app_permission
from pages.app_check_in import app_check_in
from pages.app_dining import app_dining
# from pages.app_room_nightlife import app_room_nightlife
from pages.app_login import app_login
from pages.app_network_metrics import app_network_metrics


class FlutterAppTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver() 

    def test_TestCase_A_Flutter_App_Installed(self):
        app_reset_start_time.test_1(self)
    
    def test_TestCase_B_Flutter_App_Battery_Metrics(self):
        app_battery_metrics.test_2(self)

    def test_TestCase_C_Flutter_App_Memory_Metrics(self):
        app_memory_metrics.test_3(self)

    # def test_TestCase_C_Flutter_App_Network_Metrics(self):
    #     app_network_metrics.test_4(self)

    def test_TestCase_D_Flutter_App_Permission(self):
        app_permission.test_5(self)

    def test_TestCase_E_Flutter_App_Check_In(self):
        app_check_in.test_6(self)
        
    def test_TestCase_E_Flutter_App_Dining(self):
        app_dining.test_7(self)

    def test_TestCase_E_Flutter_App_Login(self):
        app_login.test_9(self)
        

    def tearDown(self):
        time.sleep(2)
        self.driver.instance.quit()


if __name__ == '__main__':
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Flutter_App_Test_Results'))
    # all the testcase results are captured in report/Test_Results as HTML file