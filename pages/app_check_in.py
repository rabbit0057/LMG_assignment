from driver.desiredcapabilities import *
import time
import datetime
from appium.webdriver.common.touch_action import TouchAction


# Test Case for App-check-in and health check details
class app_check_in:
    def test_6(self):
        start_time = time.time() # script start time
        self.driver.instance.implicitly_wait(10)
        
        CheckInButton = self.driver.instance.find_element_by_accessibility_id("Check-In")
        CheckInButton.click()
        LOGGER.info("Check-In Button on the Home Page")

        HealthCheckPage = self.driver.instance.find_element_by_accessibility_id("Health Check")

        if HealthCheckPage.is_displayed():
            LOGGER.info("Current in HealthCheckPage ")

        touch = TouchAction(self.driver.instance)
        for i in range(1):
            touch.press(x=1004, y=1672).move_to(x=1004, y=1136).release().perform()
            LOGGER.info("HealthCheckPage Scrolling Down")

        Back = self.driver.instance.find_element_by_accessibility_id("Navigate back")
        Back.click()
        LOGGER.info("Back to Home Page")

        end_time = time.time()
        LOGGER.info("Total execution time: {} seconds".format(end_time - start_time)) # script end time