
from paver.easy import *
from paver.setuputils import setup
import threading, os, platform


setup(
    name = "behave-browserstack",
    version = "0.1.0",
    author = "BrowserStack",
    author_email = "support@browserstack.com",
    description = ("Behave Integration with BrowserStack"),
    license = "MIT",
    keywords = "example selenium browserstack",
    url = "https://github.com/browserstack/lettuce-browserstack",
    packages=['features']
)



@task
@consume_nargs(1)
def run(args):
    """Run single, local and parallel test using different config."""
    switcher = {
        "single" : "python web/single.py",
        "parallel" : "python web/parallel.py",
        "local" : "python web/local.py",
        "appium-android" : "python app/android-appium.py",
        "appium-ios" : "python app/ios-appium.py",
        "app-parallel" : "python app/parallel_app.py",
        "espresso" : "python app/espresso.py",
        "xcuitest" : "python app/xcuitest.py",
        "earlgrey" : "python app/earlgrey.py",
        "health-repo" : "python repohealth.py",

    }
    print(switcher.get(args[0],"nothing"))

    os.system(switcher.get(args[0],"nothing"))

@task
def test():
    """Run all tests"""
    sh("paver run single")
    sh("paver run local")
    sh("paver run parallel")
    sh("paver run appium-android")
    sh("paver run appium-ios")
    sh("paver run app-parallel")
    sh("paver run espresso")
    sh("paver run xcuitest")
    sh("paver run earlgrey")
    sh("paver run health-repo")
