# command.py: This program should be able to take input from the terminal and
# talk with other local libraries on how those commands should be performed

from MouseManager import MouseMover
from KeyboardManager import keyPresser


class Command():

    def __init__(self=None):
        print("Starting...")

        while (True):
            x = input("Command: ")
            if(x.upper() == "Q" or x.upper() == "QUIT"):
                break
            else:
                try:
                    parse(x)()
                except Exception as e:
                    print(e, ": Something went wrong.")
        print("Ending...")
        # TODO add terminate function here


def convert(x):
    """ This function attempts to convert and return x
    to a float and on exception, returns it as a string.
    """
    try:
        return float(x)
    except:
        return str(x)


def parse(x):
    """ This function parses x provided by the user. It can do any of the following:
    1. Move the mouse (w/ or w/o relative)
    2. Click the mouse
    3. Move (w/ or w/o relative) and click/double click

    Arguments:
    x {String} -- provided through stdin Input. In the form:
    1. moveTo {x} {y} {opt int: dur}
    2. moveToRel {x} {y} {opt int: dur}
    3. click {opt int: clicks} {opt int: right}
    5. moveClick {x} {y} {opt int: dur} {opt int: clicks} {opt int: right}
    6. relClick {x} {y} {opt int: dur} {opt int: clicks} {opt int: right}
    7. getPos
    8. string: Enter multiple commands, executed in order automatically.
    9. scroll: {val} {opt int: dur} {opt int: up}
    //Keyboard Commands
    10. type: {string}
    11. slowType: {string} {opt double delay}
    13. double: {pressed} {string}
    14. delay {s}: delays system for s seconds
    15. end: Ends execution

    Returns:
      lambda -- Returns Function to be called which will execute given inputs.
    """
    def end(*args): raise Exception("Execution Ended")
    switcher = {
        "MOVETO": lambda args: MouseMover.moveTo(*args),
        "MOVEREL": lambda args: MouseMover.moveRel(*args),
        "CLICK": lambda args: MouseMover.click(*args),
        "MOVECLICK": lambda args: MouseMover.moveClick(*args),
        "RELCLICK": lambda args: MouseMover.relClick(*args),
        "GETPOS": lambda args: MouseMover.getPos(*args),
        "STRING": lambda args: string(*args),
        "DRAGTO": lambda args: MouseMover.dragTo(*args),
        "DRAGREL": lambda args: MouseMover.dragRel(*args),
        "SCROLL": lambda args: MouseMover.scroll(*args),
        "INSTASCROLL": lambda args: MouseMover.instaScroll(*args),
        "TYPE": lambda args: keyPresser.input(*args),
        "SLOWTYPE": lambda args: keyPresser.slowType(*args),
        "DOUBLE": lambda args: keyPresser.double(*args),
        "DELAY": lambda args: MouseMover.delay(*args),
        "END": lambda args: end(*args)
    }
    func = switcher.get(x.split()[0].upper(),
                        lambda *args: print("The Function wasn't found."))
    parsedRest = list(map(lambda x: convert(x), x.split()[1:]))
    return lambda: func(parsedRest)


def string():
    print("Stringing beginning, quit with Q")
    commands = []
    while (True):
        x = input("Next Command: ")
        if(x.upper() == "Q" or x.upper() == "QUIT"):
            break
        else:
            commands.append(parse(x))
    for func in commands:
        try:
            print("Executing...")
            func()
        except Exception as e:
            print(e, ": That function couldn't be executed.")
    print("Done!")


def textCommand(filePath, termFunc):
    commands = []
    try:
        f = open(filePath, 'r')  # 'r' for read mode
        for line in f:
            if len(line) > 1 and line[:2] != "//" and line[:1] != "#":
                commands.append([parse(line), line])
            else:
                pass  # print("Skipping line...", line)

        for func in commands:
            print("Executing... ", func[1])
            func[0]()
    except Exception as e:
        print(e, ": Something went wrong")
    print("Done!")
    termFunc()
