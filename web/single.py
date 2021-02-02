from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os,time

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']

desired_cap = {
'browser': 'Chrome',
 'browser_version': 'latest',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '1024x768',
 'name': 'Python Sample Single Test',
 'build':'Python Demo',
 'browserstack.debug':'true'
}

driver = webdriver.Remote(
    command_executor='https://%s:%s@hub-cloud.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),
    desired_capabilities=desired_cap)
print("Single Test Started...")

driver.get("http://www.google.com")

time.sleep(5)
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
time.sleep(20)
elem.send_keys("BrowserStack")
elem.submit()
print (driver.title)
driver.quit()
