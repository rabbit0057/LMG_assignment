from driver.desiredcapabilities import *
import time
import datetime

# Test Case to check the time of the start for the automation.
class app_reset_start_time:
    def test_1(self):
        start_time = time.time() # script start time
        self.driver.instance.reset() # Reseting the app
        self.driver.instance.unlock() # Unlocking the app -- if locked 
        self.driver.instance.is_app_installed(TestappPackage) # to check if the app is installed 
        LOGGER.info("APP Installed")
        begin_time = datetime.datetime.strptime(str(datetime.datetime.now()), '%Y-%m-%d %H:%M:%S.%f') # App Opening Time
        LOGGER.info("APP STARTED AT: %s" % begin_time)
        end_time = time.time() # script end time
        LOGGER.info("Total execution time: {} seconds".format(end_time - start_time)) 
    
        

