# logger.py: This program should be able to log both mouse activity
# and keystrokes in order to send the program information on how to
# start and stop, as well as if input was correctly executed.

from pynput.keyboard import Listener  as KeyboardListener
from pynput.mouse    import Listener  as MouseListener
from pynput.keyboard import Key
import sys, pynput, logging, time, threading

log = (False, False)

logging.basicConfig(filename=("log.txt"), level=logging.INFO, format='%(asctime)s: %(message)s')
term = lambda: print("Terminate not set.")

class Machine:
    #TODO default_on_press must be implemented
    def on_press(self, key):
        if key == Key.esc:
            term()
        if self.log[0]:
            logging.info(str(key))
    
    def default_on_click(self, x, y, button, pressed):
        if pressed and button == pynput.mouse.Button.left:
            if self.log[1]:
                logging.info("Mouse clicked at ({0}, {1}) with {2}".format(x, y, button))

    def revertClick(self=None, func=lambda *args: None):
        """ This function takes a function as a parameter, and then alters
        the on_click function for the MouseListener so that it performs func
        after completing its usual debugging operation. Every call will revert
        any old changes made.
        Make sure that func = lambda self, x, y, button, pressed: <BODY>.
        """
        def newFunc(self, x, y, button, pressed):
            Machine.default_on_click(self, x, y, button, pressed)
            func(self, x, y, button, pressed)
        print('', end="") # For some reason, excluding a print line will not allow
        # the terminal to recognize any print functions in func. Why??
        Machine.on_click = newFunc

    def startListening(self):
        """ Starts Listeners together to avoid AttributeError: CFRunLoopAddSource.
        """
        with MouseListener(on_click=lambda x, y, button, pressed: Machine.on_click(self, x, y, button, pressed)) as listener:
            with KeyboardListener(on_press=lambda key: Machine.on_press(self, key)) as listener:
                #The above implementation delays the call to the frame,
                #allowing the class methods to be altered and replaced by files
                #externally and thus allowing the parameters to be bled elsewhere.
                listener.join()

    def __init__(self, log): #log provided at top of file
        Machine.on_click = Machine.default_on_click #Logger.default_on_click is never changed
        self.log = log #tuple [0] for Keyboard, [1] for mouse
        #This threading stops the .join function from conflicting with the main thread.
        self.thread = threading.Thread(target=Machine.startListening, args=(self,))
        self.thread.setDaemon(True)
        self.thread.start()
        
def init(terminate):
    global term
    print("Key/Mouse logger joining... Logging Status:", log)
    term = terminate
    Machine(log)