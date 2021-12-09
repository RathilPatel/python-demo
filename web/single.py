import selenium
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

driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
try:
    driver.get("http://www.google.com")
    if not "Google" in driver.title:
        raise Exception("Unable to load google page!")
    elem = driver.find_element_by_name("q")
    elem.send_keys("BrowserStack")
    elem.submit()
    print (driver.title)
    if "BrowserStack - Google Search" in driver.title:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Page Title Matched!!"}}')
    else:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Page Titled didn\'t Match! "}}')

except:
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Exception occured check Local console Log "}}')



finally:
    driver.quit()
