from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os, time ,requests
from browserstack.local import Local


BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']


bs_local = Local()
bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY }
bs_local.start(**bs_local_args)
# print ("Success starting local!!")

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '75.0',
 'os': 'Windows',
 'os_version': '7',
 'resolution': '1024x768',
 'browserstack.local' : 'true',   # LOCAl CAPABILITY
 'name': 'Python Local APIs',
 'build': 'Python Demo'
}

try:
    driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=desired_cap)
    print("Local Test Started")

    driver.get("localhost:8000") # Local Environment
    time.sleep(10)

    if "Local Server" in driver.title:
        requests.put('https://'+BROWSERSTACK_USERNAME+':'+BROWSERSTACK_ACCESS_KEY+'@api.browserstack.com/automate/sessions/'+driver.session_id+'.json', data={"status": "passed", "reason": "Local Server title matched"})
        print("Marked Test Pass using REST API") # Rest Api For Pass!
    else:
        requests.put('https://'+BROWSERSTACK_USERNAME+':'+BROWSERSTACK_ACCESS_KEY+'@api.browserstack.com/automate/sessions/'+driver.session_id+'.json', data={"status": "failed", "reason": "Local Server title not found"})
        print("Marked Test Fail using REST API") # Rest Api for Fail !

finally:
    bs_local.stop()
    driver.quit()
