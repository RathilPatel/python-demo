import os,subprocess

try:
	subprocess.call(["python3","web/single.py"])

	subprocess.call(["python3","web/parallel.py"])

	subprocess.call(["python3","web/local.py"])

	subprocess.call(["python3","app/android-appium.py"])

	subprocess.call(["python3","app/ios-appium.py"])

	subprocess.call(["python3","app/espresso.py"])

	subprocess.call(["python3","app/xcuitest.py"])

	subprocess.call(["python3","app/earlgrey.py"])




except:
	print("something Wrong!!")

# subprocess.check_call("exit 1", shell=True)

# os.system("python3 single.py")

# os.system("python3 parallel.py")

# os.system("python3 local.py")

# os.system("python3 espresso.py")

# os.system("python3 earlgrey.py")

# os.system("python3 xcuittest.py")

# os.system("python3 android-appium.py")

# os.system("python3 ios-appium.py")




