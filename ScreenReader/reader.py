# reader.py: This program should be able to take and discard screenshots,
# find the position of both certain text and images on the screen,
# and return that position.

import sys
sys.path.append('./') # When running from the folder above
sys.path.append('../') # When running from Screenreader
from PIL import Image, ImageGrab
from Logger import logger
from MouseManager import MouseMover
import pyautogui
import pynput
shotPool = []
scrnshotFolder = "./scrnshots/"  # It's assumed all pics exist here
width, height = pyautogui.size()
true_ratio = ImageGrab.grab().size[0] / width  # For high dpi screens


def takeShot(fil="", region=(0, 0, width, height)):
    print("Photo requested", fil, region)
    region = [int(x * true_ratio) for x in region]
    for i in range(2, 4):
        if region[i] < 0:
            region[i - 2] += region[i]
            region[i] *= -1
    region = tuple(region)
    try:
        if fil:
            img = pyautogui.screenshot(fil, region=region)
        img = pyautogui.screenshot(region=region)
    except Exception as e:
        print(e, ":Something went wrong with taking your photo.")
    shotPool.append(img)
    return img


def takeMouseShot():
    """ takeMouseShot awaits for two right-clicks by the user
    in order to take and possibly save a screenshot.
    It makes use of the revertClick method implemented in logger
    to allow the mouse click event to bleed into the method.
    """
    # Requires logger.init be called first in a separate thread
    # TODO possibly move Print statements to logging.
    fil = input("Select a file name to save to (Leave Empty if none) ")
    print("Awaiting First Input (Right Click)")
    first, second = [], []

    def onFirst(self, x, y, button, pressed):
        nonlocal first
        if button == pynput.mouse.Button.right and pressed:
            first = [x, y]
            print("First Received!", first,
                  "Awaiting Second Input. (Right Click)")
            logger.Machine.revertClick(func=onSecond)

    def onSecond(self, x, y, button, pressed):
        nonlocal second
        if button == pynput.mouse.Button.right and pressed:
            second = [x, y]
            print("Coords received,", second, "Taking Shot")
            takeShot(scrnshotFolder + fil,
                     (first[0], first[1], second[0] - first[0], second[1] - first[1]))
            print("Photo taken!")
            logger.Machine.revertClick()

    logger.Machine.revertClick(func=onFirst)


def locate(filName, pos="CENTER", gray=True, conf=.8):
    """ Locates given file name, returns position on screen pertaining
    to pos in ["TOP-LEFT", "MID-LEFT", "BOTTOM-LEFT", 
    "TOP-RIGHT", "MID-RIGHT", "BOTTOM-RIGHT"] by default using "CENTER".

    If given filName not valid, or if image not found, returns False.
    """
    try:
      img = Image.open(scrnshotFolder + filName)
      width, height = img.size[0], img.size[1]
    except Exception as e:
      return False
    switcher = {
        "TOP-LEFT": lambda x, y, width, height: (x, y)
        # TODO add rest of items
    }
    findPoint = switcher.get(pos.upper(), 
    lambda x, y, width, height: (x + width / 2, y + height / 2))
    try:
        info = pyautogui.locateOnScreen(scrnshotFolder + filName, 
        gray=gray, conf=conf)
        print(info)
        return findPoint(info[0], info[1], info[2], info[3])
    except Exception as e:
        return False
