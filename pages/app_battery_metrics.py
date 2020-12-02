from driver.desiredcapabilities import *
import time
import datetime

class app_battery_metrics:
    def test_2(self):
        start_time = time.time()
        LOGGER.info("CAPTURING BATTERY METRICS")
        battery = self.driver.instance.get_performance_data(TestappPackage,'batteryinfo')
        BatteryInfo = ("CURRENT BATTERY LEVEL:",*battery[1])
        LOGGER.info(BatteryInfo)
        BatteryUsedPercent = str(battery).replace('[','').replace(']','').replace("'",'').replace('power','').replace(',','')
        BatteryDiffFind = int(100) - int(BatteryUsedPercent)
        TotalBatteryUsed = ("BATTERY USED LEVEL:",BatteryDiffFind)
        LOGGER.info(TotalBatteryUsed)
        end_time = time.time()
        LOGGER.info("Total execution time: {} seconds".format(end_time - start_time))