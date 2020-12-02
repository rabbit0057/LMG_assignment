from appium import webdriver
from driver.desiredcapabilities import *
import os

class Driver:

    def __init__(self):
        # Desiredcapabilities are defined
        desired_caps = {
            "platformName": Test_mobile_type,
            "platformVersion": TestPlatformVersion,
            "deviceName": TestDeviceName,
            "automationName": TestAutomationName,
            "app": TestApkPath,
            "appPackage": TestappPackage,
            "noReset":TestNoReset,
            "appActivity":TestAppActivity,
            }
        self.instance = webdriver.Remote(TestIpPort, desired_caps)

