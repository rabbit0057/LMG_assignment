import os
import logging
from airtest.utils.logger import get_logger

# for making logging easier
LOG_LEVEL=logging.ERROR
if os.environ.get('LOG_LEVEL') == "DEBUG":
  LOG_LEVEL=logging.DEBUG
elif os.environ.get('LOG_LEVEL') == "INFO":
  LOG_LEVEL=LOG_LEVEL

## This class logger TODO:make this simpler
LOGGER = get_logger(__name__)
formatter = logging.Formatter(fmt='[Flutter_App_Automate][%(asctime)s] --- %(message)s',
   datefmt='%I:%M:%S'
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)



# Dynamically using desiredcapabilities
Test_mobile_type = "Android"
# TestApkPath= os.path.abspath(os.path.join(os.path.dirname(__file__),"apps","base.apk"))
TestApkPath = '/Users/dprakash/Documents/LMG_assignment/base.apk'
TestappPackage = 'com.mgmresorts.mgmresorts'
TestPlatformVersion = '10'
TestDeviceName = 'Samsung Galaxy note 10+'
TestAutomationName = 'UiAutomator2'
TestNoReset = True
TestAppActivity = "com.mgmresorts.mgmresorts.MainActivity"
TestIpPort = "http://0.0.0.0:4723/wd/hub"




