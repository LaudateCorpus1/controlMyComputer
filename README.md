### Readme

11 / 13 / 2020
Finally time to put those 2 months and $3K in CS61a to good use! This entire project will be written in Python. The idea is to create a program that takes Web Scraping to a whole new level.
I call it "Desktop Scraping," very original name if I do say so myself. The end result should be a program with a GUI interface where I can designate mouse "keyframes" and times. Upon execution, the program should be able to  control my mouse, read the pixels of the screen and move the mouse accordingly.
When designated, the mouse should be able to click as told, and read input
from the screen mostly in terms of text.

Alternatively, the program should also have the option to turn on "Web Scraping+." In this section, I should be able to give commands specific to the Google Chrome Browser, in the form of links to click, mouse movement, and keyboard input.  The program should be able to read certain parts of the page, even if they are not directly embedded in the HTML code.

Caveats (To be updated later on):
  1. Limit the use of outside libraries, I want my code to be as original as possible.
  2. Following the last condition, it is necessary for all MacOSes running the program to atleast install the pyautogui and pynput libraries using PIP, which installs a few dependencies they use as well. Upon research, it is hard to bypass this step since OSx especially requires XQuartz to fiddle with the mouse and keyboard securely. Run the following:
  "pip3 install pyautogui" and the same for pynput. And of course, when prompted or not, make sure to give security permissions.


Steps to Greatness:
  1. Develop a program that controls the mouse correctly.
  2. Develop a program that reads the screen by pixels (Post processing can be done using a Image to Text / AI library)
  3. Develop a program that can input from the keyboard
  4. Develop smart programs that make use of web scraping for web sites (opening browsers automatically)
  5. Develop a GUI
  6. Publish


11 / 15 / 2020
Just successfully completed the MouseManager and Command Manager basic libraries.
The implementation of pyautogui was well made. In order to make some better adjustments
for later development on the GUI, I think it will be smart to create a Mouse and Keylogger
interface. I recommend the library PynPut, tutorials found here: 
https://nitratine.net/blog/post/how-to-get-mouse-clicks-with-python/
For first steps, just hooking up the clicking system to read
and create commands in the commands text file would b fine.
Maybe even the creation of a simple GUI could be done.
After this, comes the project of reading the screen to identify
whats on it. PyAutoGUI already has a native way to find images,
perhaps that can be used. Then comes the task of familiarizing
the library with how the macOS interface looks. Near the end,
I should be able to say something like:
"Open Google Chrome"
Click on the URL bar and go to a site
Scroll down (This can be implemented soon) 200 pixels
Drag over some text, Ctrl C.
Read some graph on the page, and take a picture/read it.
Open a text file and save all of this information.

Also, an emergency eject process should be created (using
Pynput likely. And the Failsafe can be turned off.)

11 / 16 / 2020
Note for later: add support for logging over print, so as to 
remove terminal clutter.
https://nitratine.net/blog/post/how-to-get-mouse-clicks-with-python/

11 / 19 / 2020
New Dependency confirmed: opencv-python -- install numpy
~67.7 MB



--Will be delaying updates on this project to make time for other projects!