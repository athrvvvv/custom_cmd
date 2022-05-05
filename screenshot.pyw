from tkinter import *
import time
from PIL import ImageTk, Image
import pyautogui as pg
import os, sys
from datetime import datetime
main_path = (os.path.dirname(__file__))
profile = os.environ['USERPROFILE']
# Create an instance of tkinter frame or window
win = Tk()
win.title("Screenshot taker")
win.iconbitmap(os.path.join(main_path,"frontend",'screenshot.ico'))
# Set the size of the window
win.geometry("500x500")

# Define a function for taking screenshot
def screenshot():
   current = datetime.today()
   current_illusion = current.strftime("%b-%d-%Y %I-%M-%S %p")
   string_time = str(current_illusion)
   filename = (os.path.join(profile,"OneDrive\Pictures\Screenshots/"+string_time+".png"))
   ss = pg.screenshot(filename)
   win.deiconify() # REPEAT GUI

def hide_window():
   # hiding the tkinter window while taking the screenshot
   win.withdraw()
   win.after(1000, screenshot)

# Add a Label widget
Label(win, text="Click button to Screenshot", font=('Times New Roman', 18, 'bold')).pack(pady=10)

# Create a Button to take the screenshots
button = Button(win, text="Take Screenshot", font=('Aerial 11 bold'), background="#aa7bb1", foreground="white", command=hide_window)
button.pack(pady=30)

win.mainloop()
