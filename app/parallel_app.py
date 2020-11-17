import os
#  Parallel Test Trigger
os.system("pip install Appium-python-client")
os.system("python app/run_parallel_tests_app.py app/testrun_app.py app/device.json")
