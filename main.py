import time
from datetime import datetime
import random

import selenium.common.exceptions
from selenium import webdriver



def SetTimer(seconds):


    for x in range(0, seconds + 1):
        print(seconds)
        seconds = seconds - 1
        time.sleep(1)


now = datetime.now() # current date and time

emojiClass = 'reactionInner-15NvIl'
messageClass = 'container-1ov-mD'

print("Input credentials for Discord... \n")

username = input("Email: ")
password = input("Password: ")

driver = webdriver.Chrome(executable_path="chromedriver.exe")



driver.get("https://www.discord.com/login")

usernameInput = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input')
passwordInput = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')

usernameInput.send_keys(username)
passwordInput.send_keys(password)

loginButton = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
loginButton.click()

def WaitForPageToLoad():

    captchaDone = False
    while not captchaDone:
        try:
            driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/section/div[1]/h3')
            captchaDone = True
            time.sleep(1)
        except:
            print("Page not loaded, or captcha not done...")
            captchaDone = False
            time.sleep(1)

WaitForPageToLoad()

driver.execute_script('location.href = "/channels/512188534111862784/512192228282728449"')


WaitForPageToLoad()

SetTimer(5)
print("Ready to go! \n")


def NewMessageFoundAction():

    print(f'{time.ctime()}: New message found!')

    try:
        allemojis = driver.find_elements_by_class_name('reactionInner-15NvIl')
        lastreaction = allemojis[len(allemojis) - 1]
        time.sleep(random.randint(3, 7))
        lastreaction.click()
        print("Reacted.")
    except:
        print("No reaction found.")
        pass


while True:
    originalMessageSize = len(driver.find_elements_by_xpath("//span[text()='ARRR TipBot']"))

    while originalMessageSize == len(driver.find_elements_by_xpath("//span[text()='ARRR TipBot']")):

        time.sleep(1)
        CurrentTime = now.strftime("%H:%M:%S")
        print(f'{time.ctime()}: No new message')

    originalMessageSize = len(driver.find_elements_by_xpath("//span[text()='ARRR TipBot']"))



    NewMessageFoundAction()













