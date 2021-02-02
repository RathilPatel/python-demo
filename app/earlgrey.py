import requests,os,json

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']


# APP UPLOAD
###################Earlgrey App Upload #########################
response = requests.get('https://api-cloud.browserstack.com/app-automate/earlgrey/app-dirs', auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
not_uploaded = False
json_data = response.json()
for item in json_data:
	try:	
		if item["custom_id"] == "EarlgreyApp" :
			not_uploaded = True
			print("Zip Found")
			break
	except:
		print("")
if not_uploaded == False:
	print("Test Suite  Uploading...")
	files = {
    'data': (None, '{"url": "https://www.browserstack.com/app-automate/sample-apps/ios/BStack-EarlGrey-SampleApp.zip","custom_id":"EarlgreyApp"}'),
	}

	response = requests.post('https://api-cloud.browserstack.com/app-automate/earlgrey/app-dir', files=files, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))


###################Earlgrey App Upload #########################

###################Earlgrey Run Test #########################

headers = {
    'Content-Type': 'application/json',
}

data = '{"devices": ["iPhone 8 Plus-11"], "appDir": "EarlgreyApp", "deviceLogs" : "true"}'

response = requests.post('https://api-cloud.browserstack.com/app-automate/earlgrey/build', headers=headers, data=data, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))

###################Earl Run Test #########################
