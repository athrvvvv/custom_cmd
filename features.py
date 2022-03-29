import os,pyscreenshot, pygetwindow, time, psutil
import pyautogui as bot
from datetime import datetime

def current_time():
    now = datetime.now()
    time =now.strftime("%I:%M %p")
    print()
    print("CURRENT TIME: ",time)
    print()

def current_date():
    now = datetime.now()
    date = now.strftime("%d-%b-%Y")
    print()
    print("TODAY'S DATE: ",date)
    print()

def current_day():
    now = datetime.now()
    date = now.strftime("%A")
    print()
    print("TODAY'S DAY: ",date)
    print()

def kill_task():
    command = input("")
    if command == (""):
       StopIteration()
    else:
       os.system("TASKKILL /F /IM "+command+".exe")

def ss():
    current = datetime.today()
    current_illusion = current.strftime("%b-%d-%Y %I-%M-%S %p")
    string_time = str(current_illusion)
    win = pygetwindow.getWindowsWithTitle("zoom")[0] 
    win.activate()
    image = pyscreenshot.grab()
    image.save(r"C:\Users\athar\OneDrive\Pictures\Screenshots/"+string_time+".png")

def get_window_foreground():
    input01 = input("APP TO FOREGROUND: ")
    try:
        win = pygetwindow.getWindowsWithTitle(input01)[0] 
        win.activate()
    except:
        pass
        print("WHAT THE F**K.., you asking about!??")

def cmd_command():
    input1 = input("COMMAND:")
    if input1 == (""):
        StopIteration()
    else:
        try:
            os.system(input1)
        except:
            pass

def yt():
    os.system("start brave youtube.com")
        
def get_pass():
    with open(r"C:\Users\athar\OneDrive\Documents\PDR\paint.txt","r") as file:
        print(file.read())

def click():
    
    current = datetime.today()
    current_illusion = current.strftime("%b-%d-%Y %I-%M-%S %p")
    string_time = str(current_illusion)
    time.sleep(3)
    image = pyscreenshot.grab()
    image.save(r"C:\Users\athar\OneDrive\Pictures\Screenshots/"+string_time+".png")

def battery_percent():
    battery = psutil.sensors_battery()
    print()
    print("Battery percentage : ", battery.percent)
    print()

def kill_selective_tasks():
    os.system("taskkill /f /im whatsapp.exe")
    os.system("taskkill /f /im telegram.exe")
    os.system("taskkill /f /im resso.exe")

def maximize():
    bot.press("f11")
    
def opera_search():
    file1 = open("readme.txt","r")
    final_search = file1.read()
    modify = final_search.split(' ')
    modify_final = ("+".join(modify))
    os.system("start opera https://www.google.com/search?q="+modify_final)

def brave_search():
    file1 = open("readme.txt","r")
    final_search = file1.read()
    modify = final_search.split(' ')
    modify_final = ("+".join(modify))
    os.system("start brave https://www.google.com/search?q="+modify_final)