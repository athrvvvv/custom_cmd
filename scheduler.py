import os, json
import WConio2 as input_source
from datetime import date
now = date.today()
str_today = str(now)
main_path = os.path.dirname(__file__)

def priority_reader():
    with open((os.path.join(main_path,"autogenarated_files","priority_list.txt")), "r") as f:
        print("PRIORITY AS BELOW:- ")
        Lines = f.readlines()   
        count = 0
        for line in Lines:
            count += 1
            not_space = line.rstrip()
            if not_space:
                print("{}. {}".format(count, line.strip())) 
    print()

def set_on_off_prio(self):
    if self == "prio-":
        with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
            data = json.load(f)
            status = data["prio_status"]
        if status == (True):
            print("PRIORITY LIST DISPLAYING AT STARTUP: ON")
        elif status == (False):
            print("PRIORITY LIST DISPLAYING AT STARTUP: OFF")
        else:
            print("None")
    else:
        parcel = self.replace("prio-","").lower()
        if parcel == ("on") or parcel == ("off"):
            with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
                data = json.load(f)
                if parcel == ("on"):
                    change = {"prio_status":True}
                elif parcel == ("off"):
                    change = {"prio_status":False}
            data.update(change)
            with open((os.path.join(main_path,"AppConfiguration.json")),"a") as f:
                g = open((os.path.join(main_path,"AppConfiguration.json")),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
                print("Priority list Status Updated TO "+parcel.upper())
        else:
            print("You can only set status to ON or OFF")
        
def check_prio_status():
    with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
            data = json.load(f)
            status = data["prio_status"]
            if status == (True):
                priority_reader()
            elif status == (False):
                pass
            else:
                priority_reader()
            
def priority_list():
    with open((os.path.join(main_path,"autogenarated_files","priority_list.txt")),"r") as f:
        print("PRIORITY AS BELOW:- ")
        data = f.read()
        number_of_characters = len(data)
        Lines = f.readlines()   
        count = 0
        for line in Lines:
            count += 1
            not_space = line.rstrip()
            if not_space:
                print("{}. {}".format(count, line.strip()))
    print()
    if number_of_characters == 0:
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
            os.startfile(os.path.join(main_path,"autogenarated_files","priority_list.txt"))
            break
        elif "*" in input0:
            replace_task = input0.replace("*"," ")
            with open(((os.path.join(main_path,"autogenarated_files","priority_list.txt"))),"a") as np_file:
                np_file.write(replace_task+ "\n")
                break
        elif input0 == ("read"):
            with open(((os.path.join(main_path,"autogenarated_files","priority_list.txt"))),"r") as np_file:
                print("")
                print(np_file.read())
        elif input0 == ("cls"):
            print("CLEAR THE ENTIRE CONTENT OF FILE..?")
            print("YES (Y) or NO (N)")
            confirmation = input_source.getkey()
            if confirmation == ("n") or confirmation == ("N"):
                priority_list()
                break
            elif confirmation == ("y") or confirmation == ("Y"):
                file = open(((os.path.join(main_path,"autogenarated_files","priority_list.txt"))),"w")
                file.close()
                print("CLEARED THE CONTENT OF "+ '"'+"priority_list.txt"+'"')
            else:
                priority_list()
                break
        else:
            with open(((os.path.join(main_path,"autogenarated_files","priority_list.txt"))),"a") as np_file:
                np_file.write(input0+ "\n")

def quick_note():
    with open((os.path.join(main_path,"autogenarated_files","quick_note.txt")),"r") as np_file:    
            data = np_file.read()
            number_of_characters = len(data)
    if number_of_characters == 0:
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
            os.startfile((os.path.join(main_path,"autogenarated_files","quick_note.txt")))
            break
        elif "*" in input0:
            replace_task = input0.replace("*"," ")
            with open((os.path.join(main_path,"autogenarated_files","quick_note.txt")),"a") as np_file:
                np_file.write(replace_task+ "\n")
                break
        elif input0 == ("read"):
            with open((os.path.join(main_path,"autogenarated_files","quick_note.txt")),"r") as np_file:
                print("")
                print(np_file.read())
        elif input0 == ("cls"):
            print("CLEAR THE ENTIRE CONTENT OF FILE..?")
            print("YES (Y) or NO (N)")
            confirmation = input_source.getkey()
            if confirmation == ("n") or confirmation == ("N"):
                quick_note()
                break
            elif confirmation == ("y") or confirmation == ("Y"):
                file = open((os.path.join(main_path,"autogenarated_files","quick_note.txt")),"w")
                file.close()
                print("CLEARED THE CONTENT OF "+ '"'+"quick_note.txt"+'"')
            else:
                quick_note()
                break
        else:
            with open((os.path.join(main_path,"autogenarated_files","quick_note.txt")),"a") as np_file:
                np_file.write(input0+ "\n")

def todo_reader():
    with open((os.path.join(main_path,"autogenarated_files","todo.txt")), "r") as f:
        print("TODO LIST:- ")
        Lines = f.readlines()   
        count = 0
        for line in Lines:
            count += 1
            not_space = line.rstrip()
            if not_space:
                print("{}. {}".format(count, line.strip())) 
    print()

def set_on_off_todo(self):
    if self == "todo-":
        with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
            data = json.load(f)
            status = data["todo_status"]
        if status == (True):
            print("TODO LIST DISPLAYING AT STARTUP: ON")
        elif status == (False):
            print("TODO LIST DISPLAYING AT STARTUP: OFF")
        else:
            print("None")
    else:
        parcel = self.replace("todo-","").lower()
        if parcel == ("on") or parcel == ("off"):
            with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
                data = json.load(f)
            if parcel == ("on"):
                change = {"todo_status":True}
            elif parcel == ("off"):
                change = {"todo_status":False}
            data.update(change)
            with open((os.path.join(main_path,"AppConfiguration.json")),"a") as f:
                g = open((os.path.join(main_path,"AppConfiguration.json")),"r+")
                g.truncate(0)
                json.dump(data,f,indent=4)
                print("Todo list Status Updated TO "+parcel.upper())
        else:
            print("You can only set status to ON or OFF")
        
def check_todo_status():
    with open ((os.path.join(main_path,"AppConfiguration.json")),"r") as f:
            data = json.load(f)
            status = data["todo_status"]
            if status == (True):
                todo_reader()
            elif status == (False):
                pass
            else:
                todo_reader()
            
def todo():
    check_file = os.path.isfile(os.path.join(main_path,"autogenarated_files","todo.txt"))
    if check_file == (False):
        open((os.path.join(main_path,"autogenarated_files","todo.txt")),"w").close()
    with open((os.path.join(main_path,"autogenarated_files","todo.txt")),"r") as np_file:    
            data = np_file.read()
            number_of_characters = len(data)
    if number_of_characters == 0:
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
            os.startfile((os.path.join(main_path,"autogenarated_files","todo.txt")))
            break
        elif "*" in input0:
            replace_task = input0.replace("*"," ")
            with open((os.path.join(main_path,"autogenarated_files","todo.txt")),"a") as np_file:
                np_file.write(replace_task+ "\n")
                break
        elif input0 == ("read"):
            with open((os.path.join(main_path,"autogenarated_files","todo.txt")),"r") as np_file:
                print("")
                print(np_file.read())
        elif input0 == ("cls"):
            print("CLEAR THE ENTIRE CONTENT OF FILE..?")
            print("YES (Y) or NO (N)")
            confirmation = input_source.getkey()
            if confirmation == ("n") or confirmation == ("N"):
                todo()          
                break
            elif confirmation == ("y") or confirmation == ("Y"):
                file = open((os.path.join(main_path,"autogenarated_files","todo.txt")),"w")
                file.close()
                print("CLEARED THE CONTENT OF "+ '"'+"todo.txt"+'"')
            else:
                todo()
                break
        else:
            with open((os.path.join(main_path,"autogenarated_files","todo.txt")),"a") as np_file:
                np_file.write(input0+ "\n")

            