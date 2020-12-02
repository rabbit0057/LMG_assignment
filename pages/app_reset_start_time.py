from driver.desiredcapabilities import *
import time
import datetime

# test case to check if the app is installed sucessfully
class app_reset_start_time:
    def test_1(self):
        start_time = time.time()
        self.driver.instance.reset()
        self.driver.instance.unlock()
        self.driver.instance.is_app_installed(TestappPackage)
        LOGGER.info("APP Installed")
        begin_time = datetime.datetime.strptime(str(datetime.datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
        LOGGER.info("APP STARTED AT: %s" % begin_time)
        end_time = time.time()
        LOGGER.info("Total execution time: {} seconds".format(end_time - start_time))
    
        

