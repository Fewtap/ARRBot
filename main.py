import time
from datetime import datetime
import random
import winsound
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import platform
import os
import logging


def SetTimer(seconds):


    for x in range(0, seconds + 1):
        print(seconds)
        seconds = seconds - 1
        time.sleep(1)

import logging
logging.basicConfig(filename=f'logs', encoding='utf-8', level=logging.DEBUG)

now = datetime.now() # current date and time

emojiClass = 'reactionInner-15NvIl'
messageClass = 'message-2qnXI6 cozyMessage-3V1Y8y groupStart-23k01U wrapper-2a6GCs cozy-3raOZG zalgo-jN1Ica'

print("MACKES ÄLSKLINGS BOT, SUG KUK GOOGE")

print("Input credentials for Discord... \n")

username = input("Email: ")
password = input("Password: ")

if str(platform.system()) == 'Windows':
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
elif str(platform.system()) == 'Linux':
    driver = webdriver.Firefox()





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
        print(f"Message ID: {LastMessageID}")
        reactionMessageID = driver.find_element_by_css_selector(f'#{LastMessageID} + div').get_property('id')
        print(f'Reaction ID: {reactionMessageID}')
        reaction = driver.find_element_by_xpath(f'//div[@id="{reactionMessageID}"]/div[2]/div[2]/div[1]/div')
    except selenium.common.exceptions.NoSuchElementException:
        print("Emoji not found")

    print(nameoftheuser)
    x = random.randint(3, 7)
    SetTimer(x)
    try:
        ClickOnEmoji(reaction)
        winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC)
        print("Reacted.")
        logging.info(f"Reaction occurred at: {now.strftime()} \n Emoji Message ID: {reactionMessageID}")
    except Exception as e:
        print(e)

def ClickOnEmoji(emoji):
    hover = ActionChains(driver).move_to_element(emoji).perform()
    time.sleep(1)
    emoji.click()


def GetMessages():

    return driver.find_elements_by_xpath("//div[@class='message-2qnXI6 cozyMessage-3V1Y8y groupStart-23k01U wrapper-2a6GCs cozy-3raOZG zalgo-jN1Ica']")

def FilterMessages(AllMessages):

        finishedList = []


        for x in AllMessages:
            try:
                id = x.get_property('id')
                #print(id)
                nameofuser = driver.find_element_by_xpath(f"//div[@id='{id}']/div[1]/h2/span[1]/span").text
                #print(nameofuser)

                if nameofuser == "ARRR TipBot":

                    finishedList.append(x)


            except selenium.common.exceptions.NoSuchElementException:
                print("Name not found.")
                pass
            except:
                print("Other error.")


        return finishedList





while True:

    Messages = FilterMessages(GetMessages())
    print(len(Messages))
    originalMessageSize = len(Messages)
    MessageFound = False

    try:
        LastMessageID = Messages[len(Messages) - 1].get_property("id")
        MessageFound = True
    except:
        print("No message ID")
        MessageFound = False



    while originalMessageSize == len(FilterMessages(GetMessages())):

        time.sleep(1)
        CurrentTime = now.strftime("%H:%M:%S")
        print(f'{time.ctime()}: No new message')

    Messages = FilterMessages(GetMessages())
    originalMessageSize = len(FilterMessages(GetMessages()))

    LastMessageID = Messages[len(Messages) - 1].get_property("id")
    nameoftheuser = driver.find_element_by_xpath(f"//div[@id='{LastMessageID}']/div[1]/h2/span[1]/span").text

    SetTimer(5)


    NewMessageFoundAction()













