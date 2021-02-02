from appium import webdriver
from selenium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests , time , os

 
BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']



response = requests.get('https://api-cloud.browserstack.com/app-automate/recent_apps', auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
not_uploaded = False
json_data = response.json()
for item in json_data:
	try:
		if item["custom_id"] == "IOSDemoApp" :
			not_uploaded = True
			break
	except:
		print("")
if not_uploaded == False:
	files = {
    'data': (None, '{"url": "https://www.browserstack.com/app-automate/sample-apps/ios/BStackSampleApp.ipa","custom_id":"IOSDemoApp"}'),
	}

	response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', files=files, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))


desired_caps = {
    "name": "Appium Google Search Demo",
    "build": "Python iOS",
    "device": "iPhone 11",
	"app" : "IOSDemoApp",
    "browserstack.debug" : "true",
}
 

driver = webdriver.Remote("http://" + BROWSERSTACK_USERNAME + ":" + BROWSERSTACK_ACCESS_KEY + "@hub-cloud.browserstack.com/wd/hub", desired_caps)
print("Started Test")
text_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Button"))
)
text_button.click()

text_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Input"))
)
text_input.send_keys("hello@browserstack.com")

time.sleep(4)
return_key = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Return"))
)
return_key.click()

time.sleep(5)

text_output = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Output"))
)

if text_output!=None and text_output.text=="hello@browserstack.com":
  assert True
else:
  assert False

driver.quit()
