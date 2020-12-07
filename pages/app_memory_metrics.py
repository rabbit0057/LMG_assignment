from driver.desiredcapabilities import *
import time
import datetime

# battery = self.driver.get_performance_data(TestappPackage,'batteryinfo')
# cpu = self.driver.instance.get_performance_data(TestappPackage,'cpuinfo')
# memory = self.driver.instance.get_performance_data(TestappPackage,'memoryinfo')
# network = self.driver.instance.get_performance_data(TestappPackage,'networkinfo')

# Test Case to check the Memory Metrics
# Memory Metrics using Get Performance data from Appium
# http://appium.io/docs/en/commands/device/performance-data/get-performance-data/
class app_memory_metrics:
    def test_3(self):
        # start_time = time.time() # script start time
        LOGGER.info("CAPTURING MEMORY METRICS") 
        # getting memory info using memoryinfo
        memory = self.driver.instance.get_performance_data(TestappPackage,'memoryinfo')
        # indexing only memory values only
        AllMemoryInfo = memory[1]
        # Again indexing the [0] for fetching the total memory
        MemoryInfo = ("MEMORY INFO:",  AllMemoryInfo[0])
        LOGGER.info(MemoryInfo)
        MemoryInfoToCheckLeak = AllMemoryInfo[0]

        # check for condition if the memory usage is more the provided memory 
        if len(MemoryInfoToCheckLeak) > 10000000:
            LOGGER.info("MEMORY LEAK ISSUE OBSERVED")
        else:
            LOGGER.info("MEMORY IS WITHIN THE THRESHOLD")

        # end_time = time.time()
        # LOGGER.info("Total execution time: {} seconds".format(end_time - start_time)) # script end time