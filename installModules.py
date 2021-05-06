import subprocess
import sys
import time


#Installs Selenium (WebAutomation)
try:
    import selenium
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'selenium'])
    print("Selenium Installed!")
    pass

#Installs Webdriverpip
try:
    import webdriver_manager
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'webdriver-manager'])
    print("webdriver-manager Installed!")
    pass

try:
    import tkinter
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'tkinter'])
    print("TKinter Installed!")
    pass


try:
    import webdriver_manager
    import selenium
    print("All modules installed Sucessfully!")
except:
    print("Something went wrong.")


time.sleep(5)