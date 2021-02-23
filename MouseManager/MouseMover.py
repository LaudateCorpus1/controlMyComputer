# MouseMover.py: a program that should be able to retrieve and manipulate
# the mouse position on screen. It should also be able to click on command.
# On the side: the program should be able to delay clicks and perform movements
# over time.

import sys, pyautogui, time

pyautogui.PAUSE = 0
pyautogui.FailSafeException = True

def moveTo(x, y, duration=1):
    pyautogui.moveTo(x, y, duration)


def moveRel(x, y, duration=1):
    pyautogui.moveRel(x, y, duration)

def dragTo(x, y, dur=1):
  pyautogui.dragTo(x, y, duration=dur, button='left')

def dragRel(x, y, dur=1):
  pyautogui.drag(x, y, duration=dur, button='left')

def click(clicks=1, right=False):
  pyautogui.click(
      clicks=int(clicks),
      interval=.01,
      button=pyautogui.SECONDARY if bool(right) else pyautogui.PRIMARY
  )

def scroll(val, up=1):
  #Uses pynput library instead of pyautogui because of better
  #support
  from pynput.mouse import Controller
  mouse = Controller()
  for _ in range(int(val)):
    delay(1 / val)
    mouse.scroll(0, 1 if not up else -1)

def instaScroll(val, up=1):
  pyautogui.scroll(val if not up else -1 * val, _pause=False)
  
  


def moveClick(x, y, dur=1, clicks=1, right=False):
    moveTo(x, y, dur)
    click(clicks, right)


def relClick(x, y, dur=1, clicks=1, right=False):
    moveRel(x, y, dur)
    click(clicks, right)


def getPos():
    print(pyautogui.position())

def delay(seconds=1):
  time.sleep(seconds)