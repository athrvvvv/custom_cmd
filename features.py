import os,pyscreenshot, pygetwindow, time, psutil
from datetime import datetime, date, timedelta
import win32gui, win32con, win32api ,keyboard, pyautogui
from importlib import reload
main_path = (os.path.dirname(__file__))
profile = os.environ['USERPROFILE']
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
        
def click():
    current = datetime.today()
    current_illusion = current.strftime("%b-%d-%Y %I-%M-%S %p")
    string_time = str(current_illusion)
    time.sleep(3)
    image = pyscreenshot.grab()
    isonedrive = os.path.exists(os.path.join(profile,"OneDrive"))
    if isonedrive == (True):
        image.save(os.path.join(os.path.join(profile,"OneDrive\Pictures\Screenshots/"+string_time+".png")))
    else:
        image.save(os.path.join(profile,"OneDrive\Pictures\Screenshots/"+string_time+".png"))

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
    file1 = open(os.path.join(main_path,'autogenarated_files','search.txt'),"r")
    final_search = file1.read()
    if ".com" in final_search:
        os.system("start opera "+final_search)
    else:
        modify = final_search.split(' ')
        modify_final = ("+".join(modify))
        os.system("start opera https://www.google.com/search?q="+modify_final)

def brave_search(self):
    modify = self.split(' ')
    modify_final = ("+".join(modify))
    if ".com" in modify_final:
        os.system("start brave "+self)
    else:
        os.system("start brave https://www.google.com/search?q="+modify_final)
    

def clear_command_history():
    file = open(os.path.join(main_path,'autogenarated_files',"command_history.txt"),"w")
    file.close()

def check_empty_command():
    f = open(os.path.join(main_path,'autogenarated_files',"command_history.txt"),"r")
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
    check_file = os.path.exists(os.path.join(main_path,"autogenarated_files",dateee+".txt"))
    if check_file == (False):
        os.system("echo "+dateee+" >> "+(os.path.join(main_path,"autogenarated_files",dateee+".txt")))   
        f = open(os.path.join(main_path,"autogenarated_files",dateee+".txt"), "w")
        f.write("GREETED...!!")
        greet_sentence()

def del_greet_file():
    today = date.today()
    yesterdayy = today - timedelta(days = 1)
    yesterday = str(yesterdayy)
    check_file = os.path.exists(os.path.join(main_path,"autogenarated_files",yesterday+".txt"))
    if check_file == (True):
        os.system("del /f "+(os.path.join(main_path,"autogenarated_files",yesterday+".txt")))

def com(self):
    os.system("start brave "+self)

# Feature for tracking master
def check_dir():
    tracker = os.path.exists(os.path.join(main_path,'tracker'))
    status = os.path.exists(os.path.join(main_path,'tracker','status.txt'))
    track_on = os.path.exists(os.path.join(main_path,'tracker','track_on.txt'))
    autogenarated_files = os.path.exists(os.path.join(main_path,'autogenarated_files'))
    if tracker == (False):
        os.mkdir(os.path.join(main_path,'tracker'))
        os.system("attrib +h "+ os.path.join(main_path,'tracker'))
    if status == (False):
        open(os.path.join(main_path,'tracker','status.txt'),'a').close()
    if track_on == (False):
        open(os.path.join(main_path,'tracker','track_on.txt'),'a').close()
    if autogenarated_files == (False):
        os.mkdir(os.path.join(main_path,'autogenarated_files'))
        os.system("attrib +h "+ os.path.join(main_path,'autogenarated'))

def refresh_x(self):
    win32api.keybd_event(0x5B, 0, ) # LWIN
    win32api.keybd_event(0x44, 0, ) # D
    for i in range (self):
        keyboard.send("F5")
        time.sleep(0.2)
    pyautogui.hotkey("win","d")

def copy_files(self):
    check_file = os.path.exists(os.path.join(main_path,"autogenarated_files",self))
    if check_file == (False):
        print("ALERT WARNING FILE MISSING !?")     
    else: 
        thing = os.path.join(main_path,"autogenarated_files",self)
        with open (thing,"r") as file:
            lines = file.read().split()
            length_of_file = len(lines)
    ## IMPLEMENT the javascript method :)


def writer():
    check_file = os.path.exists(os.path.join(main_path,'autogenarated_files','writing.txt'))
    now = datetime.now()
    date = now.strftime("%d-%b-%Y")
    if check_file == (False):
        with open(os.path.join(main_path,'autogenarated_files','writing.txt'),"w") : pass
        print("CREATED NEW FILE !?")
    with open(os.path.join(main_path,'autogenarated_files','writing.txt'),'r') as f:
        print(f.read())
    input1 = input("MESSAGE: ")
    if input1 == (""):
        StopIteration()
    elif input1 == ("open"):
        os.system("start "+os.path.join(main_path,'autogenarated_files','writing.txt'))
    else:
        with open(os.path.join(main_path,'autogenarated_files','writing.txt'),'r') as f:
            read = f.read()
        if date in read:
            with open(os.path.join(main_path,'autogenarated_files','writing.txt'),'a') as f:
                now_time = datetime.now()
                time =now_time.strftime("%I:%M %p")
                f.write("\n"+input1+" - "+time)
        else:
            with open(os.path.join(main_path,'autogenarated_files','writing.txt'),'a') as f:
                now_timee = datetime.now()
                time =now_timee.strftime("%I:%M %p")
                f.write("\n"+"------------------------------------------------------------"+"\n"+date+"\n"+input1+" - "+time)

def reload_babu():
    import babu
    import scheduler
    import file_management
    import cleaner
    import commands
    import password_generator
    import features
    import startfile
    import tracking_master
    import processor
    reload(file_management)
    reload(scheduler)
    reload(commands)
    reload(password_generator)
    reload(features)
    reload(startfile)
    reload(tracking_master)
    reload(cleaner)
    reload(babu)
    reload(processor)