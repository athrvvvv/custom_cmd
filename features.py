import os,pyscreenshot, pygetwindow, time, psutil
from datetime import datetime, date, timedelta
import win32gui, win32con

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
    input1 = input("CMD COMMAND:")
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
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    
def opera_search():
    file1 = open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd/autogenerated_files/search.txt","r")
    final_search = file1.read()
    if ".com" in final_search:
        os.system("start opera "+final_search)
    else:
        modify = final_search.split(' ')
        modify_final = ("+".join(modify))
        os.system("start opera https://www.google.com/search?q="+modify_final)

def brave_search():
    file1 = open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd/autogenerated_files/search.txt","r")
    final_search = file1.read()
    if ".com" in final_search:
        os.system("start brave "+final_search)
    else:
        modify = final_search.split(' ')
        modify_final = ("+".join(modify))
        os.system("start brave https://www.google.com/search?q="+modify_final)

def clear_command_history():
    file = open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd/autogenerated_files/command_history.txt","w")
    file.close()

def check_empty_command():
    with open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd/autogenerated_files/command_history.txt","r") as f:
        read = f.read()
        len_read = len(read)
        if len_read == (100) or len_read > (100):
            print()
            print("EXITING...")
            print()
            time.sleep(3)
            exit()

def greet_sentence():
    now = datetime.now()
    day0 = now.strftime("%A")
    day = day0.upper()
    date = now.strftime("%d")
    month0 = now.strftime("%B")
    month = month0.upper()
    year = now.strftime("%Y")
    if date == ("01"):
        print("Hello, Today is "+day+" of "+date+"ST "+month+" "+year+" :)")
        print()
    elif date == ("02"): 
        print("Hello, Today is "+day+" of "+date+"ND "+month+" "+year+" :)")
        print()
    elif date == ("03"): 
        print("Hello, Today is "+day+" of "+date+"RD "+month+" "+year+" :)")
        print()
    elif date == ("21"):
        print("Hello, Today is "+day+" of "+date+"ST "+month+" "+year+" :)")
        print()
    elif date == ("22"): 
        print("Hello, Today is "+day+" of "+date+"ND "+month+" "+year+" :)")
        print()
    elif date == ("23"): 
        print("Hello, Today is "+day+" of "+date+"RD "+month+" "+year+" :)")
        print()
    elif date == ("31"):   
        print("Hello, Today is "+day+" of "+date+"ST "+month+" "+year+" :)")
        print()
    else:
        print("Hello, Today is "+day+" of "+date+"TH "+month+" "+year+" :)")
        print()

def greet():
    datee = date.today()
    dateee = str(datee)
    check_file = os.path.exists(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files/"+dateee+".txt")
    if check_file == (False):
        os.system("echo "+dateee+" >> "+r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files/"+dateee+".txt")    
        with open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files/"+dateee+".txt", "w") as f:
            f.write("GREETED...!!")
            greet_sentence()

def del_greet_file():
    today = date.today()
    yesterdayy = today - timedelta(days = 1)
    yesterday = str(yesterdayy)
    check_file = os.path.exists(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files/"+yesterday+".txt")
    if check_file == (True):
        os.system("del /f "+r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files\\"+yesterday+".txt")

def com():
    with open(r'C:\Users\athar\OneDrive\Documents\projects\custom_cmd/autogenerated_files/search.txt', 'r') as f:
            search = f.read()
    os.system("start brave "+search)