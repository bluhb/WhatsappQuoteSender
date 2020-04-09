import pyautogui as PGUI
import random
import time
import requests

PATH = "./MessagePictures/"
CONFIDENCE = 0.8
SEARHBOXSIZE = [350, 50]
NEWMESSAGES = 2

REGION = (500, 800, 200, 100)

WPMessageBox = [609, 867]

# Locations = [
        # [110, 190],
        # [110, 250]
        # ]

with open('Words.txt') as f:
    Names = list(f)

def init(NEWMESSAGES):
    Locations = []
    for i in range(0, NEWMESSAGES):
        print("Move to the next new message, you have 5 sec.")
        time.sleep(5)
        Locations.append(list(PGUI.position()))

    return Locations

def findNewMessage(Picture):
    Received = PGUI.locateAllOnScreen(PATH+Picture+".png", confidence=CONFIDENCE, grayscale = True)
    HighestY = 0
    ReturnMessage = None
    Return = []
    for Mess in Received:
        if Mess.top > HighestY:
            HighestY = Mess.top
            ReturnMessage = Mess
        Return.append(Mess)
    return Return

def sendMessage(Location, Message):
    Old = PGUI.position()
    PGUI.click(*Location)
    time.sleep(0.001)
    PGUI.typewrite(Message, interval = 0.01)
    PGUI.typewrite(["enter"])
    PGUI.moveTo(*Old)
    return None

def getQuote():
    R = requests.get('https://api.quotable.io/random')
    if R.status_code == 200:
        Data = R.json()
        Message = "{} - {}".format(Data["content"], Data["author"])
    else:
        Message = "Failed to retrieve quote"
    return Message

def getName():
    return random.choice(Names)


Locations = init(NEWMESSAGES)
print(Locations)
while True:
    QuoteList = findNewMessage("Quote")
    for Received in QuoteList:
        for Location in Locations:
            if Received.left > Location[0] and Received.left < Location[0] + SEARHBOXSIZE[0]:
                if Received.top > Location[1] and Received.top < Location[1] + SEARHBOXSIZE[1]:
                    print("Received:  {} -- Location: {}".format(Received, Location))
                    sendMessage(Location, getQuote())
                    break

    NameList = findNewMessage("Name")
    for Received in NameList:
        for Location in Locations:
            if Received.left > Location[0] and Received.left < Location[0] + SEARHBOXSIZE[0]:
                if Received.top > Location[1] and Received.top < Location[1] + SEARHBOXSIZE[1]:
                    print("Received:  {} -- Location: {}".format(Received, Location))
                    sendMessage(Location, getName())
                    break
