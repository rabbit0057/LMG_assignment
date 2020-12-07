from driver.desiredcapabilities import *
import time
import datetime

# Test Case to check the Battery Metrics
# Battery Metrics using Get Performance data from Appium
# http://appium.io/docs/en/commands/device/performance-data/get-performance-data/
class app_battery_metrics:
    def test_2(self):
        start_time = time.time()  # script start time
        LOGGER.info("CAPTURING BATTERY METRICS")
        battery = self.driver.instance.get_performance_data(TestappPackage,'batteryinfo') # getting battery info using batteryinfo
        BatteryInfo = ("CURRENT BATTERY LEVEL:",*battery[1]) # fetching the current battery level
        LOGGER.info(BatteryInfo)
        # fetching only battery percentage and replacing with  unnecessary value
        BatteryUsedPercent = str(battery).replace('[','').replace(']','').replace("'",'').replace('power','').replace(',','')
        BatteryDiffFind = int(100) - int(BatteryUsedPercent) # diff b/w total-current to check used battery percentage
        TotalBatteryUsed = ("BATTERY USED LEVEL:",BatteryDiffFind)
        LOGGER.info(TotalBatteryUsed)
        end_time = time.time()
        LOGGER.info("Total execution time: {} seconds".format(end_time - start_time)) # script end time