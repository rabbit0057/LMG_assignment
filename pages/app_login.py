from driver.desiredcapabilities import *
import time
import datetime
from appium.webdriver.common.touch_action import TouchAction
import os
from selenium.common.exceptions import NoSuchElementException

class app_login:
    def test_9(self):
        start_time = time.time()
        self.driver.instance.implicitly_wait(10)

        try:
            MeTab = self.driver.instance.find_element_by_accessibility_id("Me\nTab 4 of 4")
            MeTab.click()
        except NoSuchElementException:
            LOGGER.info("Me Tab Not visible in Home Screen")

        try:
            Login  = self.driver.instance.find_element_by_accessibility_id("Log In")
            Login.click()
        except NoSuchElementException:
            LOGGER.info("Log In Not visible in Me Tab")

        LoginWelcomeScreen = self.driver.instance.find_element_by_accessibility_id("Welcome back")
        Email = self.driver.instance.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
        Password = self.driver.instance.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
        LoginButton = self.driver.instance.find_element_by_accessibility_id("Log In")
        
        try: 
            Email.click()
            LOGGER.info("Entering Email and Password")
            os.system("adb shell input text rabbit0057@gmail.com")
            Password.click()
            os.system("adb shell input text Incorrect@57")
            LOGGER.info("Confirming Log-in")
            LoginButton.click()
        except NoSuchElementException:
            LOGGER.info("ERROR with Login Screen")

        NotNow = self.driver.instance.find_element_by_accessibility_id("Not Now")
        NotNow.click()

        time.sleep(10)
        self.driver.instance.implicitly_wait(10)
        Info = self.driver.instance.find_element_by_accessibility_id("My Info")
        LOGGER.info("Confirming Log-in Sucessfully")
        LOGGER.info("Checking My Info")
        Info.click()
        
        Back = self.driver.instance.find_element_by_accessibility_id("Navigate back")
        Back.click()
        AppSettings = self.driver.instance.find_element_by_accessibility_id("App Settings")
        AppSettings.click()
        LOGGER.info("Checking App Settings")
        Back.click()
        end_time = time.time()
        LOGGER.info("Total execution time: {} seconds".format(end_time - start_time))


        





    



        

        

