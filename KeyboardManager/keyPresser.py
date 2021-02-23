# keyPresser.py: A program that allows control over the keyboard
# with the addition of a few utility functions and possibly
# a memory bank.

from pynput.keyboard import Key, Controller
import sys, time
keyboard = Controller()
  
def double(a, b):
  for char in b:
    with keyboard.pressed(a):
      keyboard.press(char)
      keyboard.release(char)

def input(a):
  keyboard.type(a)

def slowType(a, delay=1):
  for char in a:
    time.sleep(delay)
    keyboard.press(char)
    keyboard.release(char)