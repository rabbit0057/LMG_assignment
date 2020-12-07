from driver.desiredcapabilities import *
import time
import datetime
from appium.webdriver.common.touch_action import TouchAction


# Test Case to find resturent and also check the filter of Cuisine,Meal type,Region
class app_dining:
    def test_7(self):
        start_time = time.time() # script start time
        self.driver.instance.implicitly_wait(10)

        Dining = self.driver.instance.find_element_by_accessibility_id("Dining")
        Dining.click()
        LOGGER.info("Verified current screen is in Dining ")

        FiltersForDining = self.driver.instance.find_element_by_accessibility_id("Filters")
        FiltersForDining.click()
        LOGGER.info("Filter Dining Options")


        American = self.driver.instance.find_element_by_accessibility_id("American - Unselected")
        Breakfast = self.driver.instance.find_element_by_accessibility_id("Breakfast - Unselected")
        

        if American.is_displayed():
            American.click()
            LOGGER.info("Select American'")
            if Breakfast.is_displayed():
                Breakfast.click()
                LOGGER.info("Select Breakfast")
        else:
            LOGGER.info("ERROR")

        # Performing Scrolling
        touch = TouchAction(self.driver.instance)
        for i in range(2):
            touch.press(x=990, y=1602).move_to(x=993, y=680).release().perform()

        SelectCity = self.driver.instance.find_element_by_accessibility_id("Las Vegas - Unselected")
        SelectHotel = self.driver.instance.find_element_by_accessibility_id("Bellagio Hotel & Casino - Unselected")

        if SelectCity.is_displayed():
            SelectCity.click()
            LOGGER.info("Region Selected as Las Vegas")
        else:
            LOGGER.info("ERROR")

        ApplyInDinning = self.driver.instance.find_element_by_accessibility_id("Apply")
        ApplyInDinning.click()
        LOGGER.info("Apply Dinning Filter")

        Back = self.driver.instance.find_element_by_accessibility_id("Navigate back")
        Back.click()
        LOGGER.info("Back to Home Page")


        Entertainment = self.driver.instance.find_element_by_accessibility_id("Entertainment")
        Entertainment.click()
        LOGGER.info("Entertainment Button on the Home Page")

        
        Dates = self.driver.instance.find_element_by_accessibility_id("Dates")

        if Dates.is_displayed():
            Dates.click()
            LOGGER.info("Select the Dates for Entertainment ")
        else:
            LOGGER.info("ERROR")

        Dining = self.driver.instance.find_element_by_accessibility_id("Date Range")
        Dining.click()
        LOGGER.info("Verified current screen is in Date Range ")

        Date18 = self.driver.instance.find_element_by_xpath("(//android.widget.Button[@content-desc=\"18\"])[2]")
        Date18.click()

        ApplyInDinning.click()
        LOGGER.info("Apply Dinning Filter")

        FiltersForEntertainment = self.driver.instance.find_element_by_accessibility_id("Filters")
        

        if FiltersForEntertainment.is_displayed():
            FiltersForEntertainment.click()
            LOGGER.info("Applying filters in Entertainment")
        else:
            LOGGER.info("ERROR")

        Concerts = self.driver.instance.find_element_by_accessibility_id("Concerts - Unselected")
        Concerts.click()
        LOGGER.info("Select Concerts in filters")

        LasVegas = self.driver.instance.find_element_by_accessibility_id("Las Vegas - Unselected")
        LasVegas.click()
        LOGGER.info("Select LasVegas in filters")

        ApplyInDinning.click()
        LOGGER.info("Apply Dinning Filter")

        Back.click()
        LOGGER.info("Back to Home Page")


        end_time = time.time()
        LOGGER.info("Total execution time: {} seconds".format(end_time - start_time)) # script end time
    