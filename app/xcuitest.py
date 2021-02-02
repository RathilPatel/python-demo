import requests,os,json

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']


# APP UPLOAD
# app
###################XCUITest App Upload #########################
response = requests.get('https://api-cloud.browserstack.com/app-automate/recent_apps', auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
not_uploaded = False
json_data = response.json()
for item in json_data:
	try:
		if item["custom_id"] == "XCUIApp" :
			not_uploaded = True
			print("Found App")
			break
	except:
		print("")
if not_uploaded == False:
	print("App Uploading...")
	files = {
    'data': (None, '{"url": "https://www.browserstack.com/app-automate/sample-apps/ios/BrowserStack-SampleApp.ipa","custom_id":"XCUIApp"}'),
	}

	response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', files=files, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
	print(response.status_code)


###################XCUITest App Upload #########################

###################XCUITest Test App Upload #########################
response = requests.get('https://api-cloud.browserstack.com/app-automate/xcuitest/test-suites', auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
not_uploaded = False
json_data = response.json()
for item in json_data:
	try:
		if item["custom_id"] == "XCUITestApp" :
			not_uploaded = True
			print("Found Test Suite")
			break
	except:
		print("")
if not_uploaded == False:
	print("Test Suite Uploading...")
	files = {
    'data': (None, '{"url": "https://www.browserstack.com/app-automate/sample-apps/ios/BrowserStack-SampleXCUITest.zip","custom_id":"XCUITestApp"}'),
	}

	response = requests.post('https://api-cloud.browserstack.com/app-automate/xcuitest/test-suite', files=files, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))


###################XCUITest Test App Upload #########################


###################XCUITest Run Test #########################

headers = {
    'Content-Type': 'application/json',
}

data = '{"devices": ["iPhone 8 Plus-11"], "app": "XCUIApp", "deviceLogs" : "true", "testSuite": "XCUITestApp", "project": "XcuiTestSuite"}'

response = requests.post('https://api-cloud.browserstack.com/app-automate/xcuitest/build', headers=headers, data=data, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))

###################XCUITest Run Test #########################








