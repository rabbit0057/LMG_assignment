from driver.desiredcapabilities import *
import time
import datetime

# battery = self.driver.instance.get_performance_data(TestappPackage,'batteryinfo')

# battery = self.driver.get_performance_data(TestappPackage,'batteryinfo')
# cpu = self.driver.instance.get_performance_data(TestappPackage,'cpuinfo')
# memory = self.driver.instance.get_performance_data(TestappPackage,'memoryinfo')
# network = self.driver.instance.get_performance_data(TestappPackage,'networkinfo')

class app_memory_metrics:
    def test_3(self):
        start_time = time.time()
        LOGGER.info("CAPTURING MEMORY METRICS")
        memory = self.driver.instance.get_performance_data(TestappPackage,'memoryinfo')
         # os.system("adb shell top  | grep mgm")
        AllMemoryInfo = memory[1]
        MemoryInfo = ("MEMORY INFO:",  AllMemoryInfo[0])
        LOGGER.info(MemoryInfo)
        MemoryInfoToCheckLeak = AllMemoryInfo[0]

        if len(MemoryInfoToCheckLeak) > 10000000:
            LOGGER.info("MEMORY LEAK ISSUE OBSERVED")
        else:
            LOGGER.info("MEMORY IS WITHIN THE THRESHOLD")

        end_time = time.time()
        LOGGER.info("Total execution time: {} seconds".format(end_time - start_time))