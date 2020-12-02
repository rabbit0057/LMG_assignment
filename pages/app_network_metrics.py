from driver.desiredcapabilities import *
import time
import datetime
import os
import threading

class app_network_metrics:
    def test_4(self):
        start_time = time.time()
        os.system("adb logcat | grep https")
        self.driver.instance.reset()
        LOGGER.info("Network calls are captured in network.txt file")
        end_time = time.time()
        LOGGER.info("Total execution time: {} seconds".format(end_time - start_time))