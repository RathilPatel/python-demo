from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import  sys, json

json_name = sys.argv[1]
USERNAME = "rathildemo"
BROWSERSTACK_ACCESS_KEY = "QdxLbeazV7hKoFxqXbaT"

with open(json_name, "r") as f:
    obj = json.loads(f.read())

instance_caps= obj[int(sys.argv[2])]
print ("Test "+sys.argv[2]+" started")

#------------------------------------------------------#
# Mention any other capabilities required in the test

#------------------------------------------------------#

caps = dict(instance_caps.items())
# caps = Merge(dict(caps.items()),dict(instance_caps.items()))

#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE

driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)
driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print (driver.title)
driver.quit()
