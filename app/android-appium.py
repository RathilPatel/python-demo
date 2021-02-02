from appium import webdriver
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
		if item["custom_id"] == "AndroidDemoApp" :
			not_uploaded = True
			break
	except:
		print("")
if not_uploaded == False:
	files = {
    'data': (None, '{"url": "https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk","custom_id":"AndroidDemoApp"}'),
	}

	response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', files=files, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))


desired_caps = {
    "name": "Appium Google Search Demo",
    "build": "Python android ",
	"os_version" : "10.0",
	"device" : "OnePlus 7T",
	"app" : "AndroidDemoApp",
}
 

driver = webdriver.Remote("http://" + BROWSERSTACK_USERNAME + ":" + BROWSERSTACK_ACCESS_KEY + "@hub-cloud.browserstack.com/wd/hub", desired_caps)
print("Started Test")
search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()

search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")
time.sleep(5)

search_results = driver.find_elements_by_class_name("android.widget.TextView")
assert(len(search_results) > 0)

driver.quit()