import os
import WConio2 as IS
from datetime import date
import time, datetime
now = date.today()
str_today = str(now)

def priority_list():
    check_file = os.path.isfile(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\priority_list.txt")
    if check_file == (False):
        os.system("echo> "+r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\priority_list.txt")
    
    with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\priority_list.txt", "r") as np_file:    
            data = np_file.read()
            number_of_characters = len(data)
    if number_of_characters == 12 or number_of_characters == 0:
        print()
        print("EMPTY FILE AF")
        print()
    else:
        print("")
        print(data)
        
    while True:
        input0 = input("TYPE PRIORITIES (PRESS ENTER): ")
        if input0 == (""):
            break
        elif input0 == ("open"):
            os.startfile(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\priority_list.txt")
            break
        elif "*" in input0:
            replace_task = input0.replace("*"," ")
            with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\priority_list.txt", "a") as np_file:
                np_file.write(replace_task+ "\n")
                break
        elif input0 == ("read"):
            with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\priority_list.txt", "r") as np_file:
                print("")
                print(np_file.read())
        elif input0 == ("cls"):
            print("CLEAR THE ENTIRE CONTENT OF FILE..?")
            print("YES (Y) or NO (N)")
            confirmation = IS.getkey()
            if confirmation == ("n") or confirmation == ("n"):
                priority_list()
   
            else:
                file = open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\priority_list.txt","w")
                file.close()
                print("CLEARED THE CONTENT OF "+ '"'+"priority_list.txt"+'"')
        else:
            with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\priority_list.txt", "a") as np_file:
                np_file.write(input0+ "\n")

def quick_note():
    check_file = os.path.isfile(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\quick_note.txt")
    if check_file == (False):
        os.system("echo> "+r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\quick_note.txt")
    with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\quick_note.txt", "r") as np_file:    
            data = np_file.read()
            number_of_characters = len(data)
    if number_of_characters == 12 or number_of_characters == 0:
        print()
        print("EMPTY FILE AF")
        print()
    else:
        print("")
        print(data)
    while True:
        input0 = input("TYPE QUICKY: ")
        if input0 == (""):
            break
        elif input0 == ("open"):
            os.startfile(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\quick_note.txt")
            break
        elif "*" in input0:
            replace_task = input0.replace("*"," ")
            with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\quick_note.txt", "a") as np_file:
                np_file.write(replace_task+ "\n")
                break
        elif input0 == ("read"):
            with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\quick_note.txt", "r") as np_file:
                print("")
                print(np_file.read())
        elif input0 == ("cls"):
            print("CLEAR THE ENTIRE CONTENT OF FILE..?")
            print("YES (Y) or NO (N)")
            confirmation = IS.getkey()
            if confirmation == ("n") or confirmation == (""):
                quick_note()
   
            else:
                file = open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\quick_note.txt","w")
                file.close()
                print("CLEARED THE CONTENT OF "+ '"'+"quick_note.txt"+'"')
        else:
            with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\quick_note.txt", "a") as np_file:
                np_file.write(input0+ "\n")

def roadmap():
    check_file = os.path.isfile(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\roadmap.txt")
    if check_file == (False):
        os.system("echo> "+r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\roadmap.txt")
    with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\roadmap.txt", "r") as np_file:    
            data = np_file.read()
            number_of_characters = len(data)
    if number_of_characters == 12 or number_of_characters == 0:
        print()
        print("EMPTY FILE AF")
        print()
    else:
        print("")
        print(data)
    while True:
        input0 = input("TYPE LINE: ")
        if input0 == (""):
            break
        elif input0 == ("open"):
            os.startfile(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\roadmap.txt")
            break
        elif "*" in input0:
            replace_task = input0.replace("*"," ")
            with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\roadmap.txt", "a") as np_file:
                np_file.write(replace_task+ "\n")
                break
        elif input0 == ("read"):
            with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\roadmap.txt", "r") as np_file:
                print("")
                print(np_file.read())
        elif input0 == ("cls"):
            print("CLEAR THE ENTIRE CONTENT OF FILE..?")
            print("YES (Y) or NO (N)")
            confirmation = IS.getkey()
            if confirmation == ("n") or confirmation == (""):
                roadmap()
            
            else:
                file = open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\roadmap.txt","w")
                file.close()
                print("CLEARED THE CONTENT OF "+ '"'+"roadmap.txt"+'"')
        else:
            with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\roadmap.txt", "a") as np_file:
                np_file.write(input0+ "\n")

# def tempo_timer():
#     input1,input2 = input("ENTER TIMER (HH:MM): ").split()
#     check_file = os.path.isfile(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\quick_note.txt")
#     if check_file == (False):
#         os.system("echo> tempo_timer.pyw")
#     with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\tempo_timer.py", "w") as np_file:
#             np_file.write("from datetime import datetime"+"\n"+"import pygetwindow"+"\n"+"from playsound import playsound"+"\n"+"from win10toast import ToastNotifier"+"\n"+"win = pygetwindow.getWindowsWithTitle"+"("+'"'+"py.exe"+'"'+")"+"[0]"+"\n"+"win.activate()"+"\n"+"n = ToastNotifier()"+"\n"+"while True:"+"\n"+"    "+"now "+ "=" +" datetime.now()"+"\n"+"    "+"now_current "+ "="+ " now.strftime"+"("+'"'+"%I:%M "+'"'+")"+"\n"+"    "+"now_p = "+ "now.strftime"+"("+'"'+"%p"+'"'+")"+"\n"+"    "+"if now_current <= " +"("+'"'+input1+":"+input2+'"'+"+"+" now_p"+")"+":"+"\n"+"       "+"playsound"+"("+"r"+'"'+r"C:\Users\athar\Music\music\sage_ringtone.mp3"+'"'+")"+"\n"+"       ")

def countdown(h, m, s):
 
    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
 
    print("Bzzzt! The countdown is at zero seconds!")
 
    # Inputs for hours, minutes, seconds on timer
    h = input("Enter the time in hours: ")
    m = input("Enter the time in minutes: ")
    s = input("Enter the time in seconds: ")
    # countdown(int(h), int(m), int(s))
