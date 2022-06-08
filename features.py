import os,pygetwindow, time, psutil, json
from datetime import datetime, date, timedelta
import win32gui, win32con, win32api ,keyboard, pyautogui
main_path = str(os.path.dirname(__file__))
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
        print("WHAT THE HECK.., you asking about!??")

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

def brave_search(self):
    modify = self.split(' ')
    modify_final = ("+".join(modify))
    if ".com" in modify_final:
        os.system("start brave "+self)
    else:
        os.system("start brave https://www.google.com/search?q="+modify_final)

def write_empty(self):
    if self == "write":
        with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
            data = json.load(f)
            count_number = data["command_history"]
            count = count_number + 1
            y = {"command_history":count}
            data.update(y)
        with open((os.path.join(main_path,"AppConfiguration.json")),"a") as f:
            g = open((os.path.join(main_path,"AppConfiguration.json")),"r+")
            g.truncate(0)
            json.dump(data,f,indent=4)
    if self == "check_count":
        with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
            data = json.load(f)
            len_read = data["command_history"]
        if len_read == (20) or len_read > (20):
            with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
                data = json.load(f)
                count_number = data["command_history"]
                y = {"command_history":0}
                data.update(y)
            with open((os.path.join(main_path,"AppConfiguration.json")),"a") as f:
                g = open((os.path.join(main_path,"AppConfiguration.json")),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
            print()
            print("EXITING...")
            print()
            time.sleep(3)
            exit()
    elif self == ("clear"):
        with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
            data = json.load(f)
            count_number = data["command_history"]
            y = {"command_history":0}
            data.update(y)
        with open((os.path.join(main_path,"AppConfiguration.json")),"a") as f:
            g = open((os.path.join(main_path,"AppConfiguration.json")),"r+")
            g.truncate(0)
            json.dump(data,f,indent=4)

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

def visit_counter(self):
    if self == ("count"):
        with open((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
            data = json.load(f)
        count = data["visit_count"] + 1
        y = {"visit_count":count}
        data.update(y)
        with open((os.path.join(main_path,"AppConfiguration.json")),"a") as f:
            g = open((os.path.join(main_path,"AppConfiguration.json")),"r+")
            g.truncate(0)
            json.dump(data,f,indent=4)
    elif self == ("log"):
        with open((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
            data = json.load(f)
            count_today = data["visit_count"]
            count_yesterday = data["visit_yesterday"]
            print("CUSTOM_CMD was opened "+str(count_today)+" times today :)")
            print("CUSTOM_CMD was opened "+str(count_yesterday)+" times yesterday :)")

def greet():
    today = date.today()
    with open((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
        data = json.load(f)
        greet_stat = data["greet_status"]
        if greet_stat != str(today):
            y = {"greet_status":str(today)}
            data.update(y)
            with open((os.path.join(main_path,"AppConfiguration.json")),"a") as f:
                g = open((os.path.join(main_path,"AppConfiguration.json")),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
                greet_sentence()

def com(self):
    os.system("start brave "+self)

def check_AppConfig():
    yesterday = date.today() - timedelta(days = 1 )
    tracker = os.path.exists(os.path.join(main_path,'tracker'))
    imp_code = os.path.exists(os.path.join(main_path.replace("\custom_cmd",""),"imp_code"))
    dummy_folder = os.path.exists(os.path.join((os.path.dirname(main_path)),"dummy_folder"))
    appconfig = os.path.exists(os.path.join(main_path,"AppConfiguration.json"))
    check_prio = os.path.isfile(os.path.join(main_path,"autogenarated_files","priority_list.txt"))
    check_qn = os.path.isfile(os.path.join(main_path,"autogenarated_files","quick_note.txt"))
    if check_qn == (False):
        open((os.path.join(main_path,"autogenarated_files","quick_note.txt")),"w").close()
    if check_prio == (False):
        open((os.path.join(main_path,"autogenarated_files","priority_list.txt")),"w").close()
    if tracker == (False):
        os.mkdir(os.path.join(main_path,'tracker'))
        os.system("attrib +h "+ '"' +os.path.join(main_path,'tracker')+'"')
    if imp_code == (False):
        os.mkdir(os.path.join(main_path.replace("\custom_cmd",""),"imp_code"))
    if dummy_folder == (False):
        os.mkdir(os.path.join((os.path.dirname(main_path)),"dummy_folder"))
        os.system("attrib +h "+ '"'+os.path.join(main_path,'dummy_folder')+'"')
    if appconfig == (False):
        open(os.path.join(main_path,"AppConfiguration.json"),"a").close()
        os.system("attrib +h "+ '"'+os.path.join(main_path,'AppConfiguration.json')+'"')
        dictionary = {
            'version':'v1.0.0',
            'command_history':0,
            'counter':None,
            'open_file_npp':None,
            'todo_status':None,
            'prio_status':None,
            'start_time':None,
            'last_time':None,
            'visit_count':0,
            'visit_yesterday':0,
            'greet_status':str(yesterday),
            'MSWORD':None}
        json_object = json.dumps(dictionary,indent=4)
        f = open(os.path.join(main_path,"AppConfiguration.json"),"a")
        f.write(json_object)
        f.close()
    if os.stat(os.path.join(main_path,"AppConfiguration.json")).st_size == 0:
        dictionary = {
            'version':'v1.0.0',
            'command_history':0,
            'counter':None,
            'open_file_npp':None,
            'todo_status':None,
            'prio_status':None,
            'start_time':None,
            'last_time':None,
            'visit_count':0,
            'visit_yesterday':0,
            'greet_status':str(yesterday),
            'MSWORD':None}
        json_object = json.dumps(dictionary,indent=4)
        f = open(os.path.join(main_path,"AppConfiguration.json"),"a")
        f.write(json_object)
        f.close()
        
def refresh_x(self):
    win32api.keybd_event(0x5B, 0, )
    win32api.keybd_event(0x44, 0, )
    for i in range (self):
        keyboard.send("F5")
        time.sleep(0.2)
    pyautogui.hotkey("win","d")

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
                
def bluetooth(self):
    selff = self.strip()
    if selff == "on":
        os.system("powershell -command {} -BluetoothStatus On".format(os.path.join(main_path,"bluetooth.ps1")))
    elif selff == "off":
        os.system("powershell -command {} -BluetoothStatus Off".format(os.path.join(main_path,"bluetooth.ps1")))
    else:
        print("ONLY ACCEPTS ON AND OFF")

def auto_bs_search(self):
    if "pip install " in self or "PIP INSTALL " in self:
        StopIteration()
    else:
        split_it_baby = self.split()
        length = len(split_it_baby)
        if length > 2:
            print("SEARCH")
            modify = self.split(' ')
            modify_final = ("+".join(modify))
            os.system("start brave https://www.google.com/search?q="+modify_final)

def greet_time():
    current_hour = int(datetime.now().strftime('%H'))
    if current_hour >= 5 and current_hour <= 12:
        print('Good Morning..')
        print()
    elif current_hour >=23 and current_hour >=5:
        print("You should sleep now")
    elif 12<=current_hour<=18:
        print('Good Afternoon..')
        print()
    else:
        print('Good Evening..')
        print()

def mute_speakers():
    # subprocess.call("cscript.exe "+os.path.join(main_path,"mute.vbs"))
    os.system(os.path.join(main_path,"mute.vbs"))

def write_time():
    time.time()
    start_time = time.time()
    now = datetime.now()
    time_note =now.strftime("%I:%M %p")
    with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
        data = json.load(f)
    change = {"start_time":start_time,"last_time":time_note}
    data.update(change)
    with open((os.path.join(main_path,"AppConfiguration.json")),"a") as f:
        g = open((os.path.join(main_path,"AppConfiguration.json")),"r+")
        g.truncate(0)
        json.dump(data,f,indent=4)

def read_visited_time():
    time.time()
    end_time = time.time()
    f = open(os.path.join(main_path,"AppConfiguration.json"))
    y = json.load(f)
    start = y['start_time']
    last_time = y['last_time']
    n = (end_time-start)
    diff_hour = time.strftime("%H", time.gmtime(n))
    #diff_hour = time.strftime("%H:%M:%S", time.gmtime(n))
    if int(diff_hour) > 0 :
        print("LASTLY VISITED "+diff_hour+" HOURS AGO AT "+last_time)
        print()
    else:
        print("LASTLY VISITED RECENTLY")

def wifi(self):
    if " off" in self:
        os.system("netsh wlan disconnect")
    elif " on" in self:
        os.system("netsh wlan connect name=Nidhi")
    else:
        print("ONLY ACCEPTS ON OR OFF")  