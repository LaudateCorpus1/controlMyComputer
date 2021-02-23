# main.py: In charge of starting and ending execution.
# 11 / 17 / 2020: A slight oversight was made, which caused me to reconsider
# how I was going to create this main file. Essentially, the main file will
# act as a "Process Manager" where every function called will spawn a seperate
# thread, and the end of the program will involve a while loop that will
# raise exceptions where needed. At this point, that will only be in the
# Keylogger thread.
from CommandManager.command import Command, textCommand
import Logger, ScreenReader
import sys
import pyautogui
import time
import threading


threadPool, running, terminateMessage = [], True, ""


def terminate(message="The program was quit."):
    global running, terminateMessage
    running, terminateMessage = False, message


def spawnThread(func, args=()):
    thread = threading.Thread(target=func, args=args)
    thread.setDaemon(True)
    thread.start()
    threadPool.append(thread)


def inf():
    while(True):
        time.sleep(1)
        print(pyautogui.position())


# TODO: Extend implementation to allow restarting,
# moving from function to function. Adding a parameter to terminate^ will
# allow more control over the flow.
def begin():
    spawnThread(Logger.logger.init, (terminate,))
    #  Example of Revert Click Below:
    #  logger.Machine.revertClick(func=lambda self, x, y, button, pressed: print(x, y))
    if len(sys.argv[1:]) == 0:
        spawnThread(textCommand, ("./commands.txt", terminate))
    elif sys.argv[1] == 'man':
        spawnThread(Command)
    elif sys.argv[1] == 'pic':
        spawnThread(ScreenReader.reader.takeMouseShot)
    else:
        spawnThread(inf)


begin()
try:
    while running:
        pass
    raise Exception(terminateMessage)
except Exception as e:
    print(e, "Exiting...")