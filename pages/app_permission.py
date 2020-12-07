from driver.desiredcapabilities import *
import time
import datetime
from selenium.common.exceptions import NoSuchElementException


# Test case to check the app permission related functionality
class app_permission:
    def test_5(self):
        start_time = time.time() # script start time
        self.driver.instance.implicitly_wait(10)


        # checking permissions Agree & Continue if not raise a NoSuchElementException 
        try:
            AgreeContinue = self.driver.instance.find_element_by_accessibility_id("Agree & Continue")
            AgreeContinue.click()
            LOGGER.info("Accepted Agree & Continue")
        except NoSuchElementException:
            print("Agree and Continue Button not found the screen")

            
        Continue = self.driver.instance.find_element_by_accessibility_id("Continue")
        Continue.click()

        # Allow permission for location
        AppPermissionLocation = self.driver.instance.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button")
        AppPermissionLocation.click()
        LOGGER.info("App Permission allowed")

        Close = self.driver.instance.find_element_by_accessibility_id("Close")
        Close.click()
        LOGGER.info("Travel and Property Opening Infomation")

        Dismiss = self.driver.instance.find_element_by_accessibility_id("Dismiss")
        Dismiss.click()
        LOGGER.info("Going Home Screen")
    
        end_time = time.time()
        LOGGER.info("Total execution time: {} seconds".format(end_time - start_time)) # script end time