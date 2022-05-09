import os
import WConio2 as input_source
from datetime import date
now = date.today()
str_today = str(now)

main_path = os.path.dirname(__file__)

def priority_reader():
    with open((os.path.join((os.path.dirname(main_path)),"autogenarated_files","priority_list.txt")),"r") as f:
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
    with open((os.path.join(main_path,"autogenarated_files","prio_status.txt")), "w") as f:
        status = self.lower()
        f.write(status)
        
def check_prio_status():
    with open((os.path.join(main_path,"autogenarated_files","prio_status.txt")), "r") as f:
        read = f.read()
        if read == ("on"):
            priority_reader()
        else:
            StopIteration()
def priority_list():
    check_file = os.path.isfile(os.path.join(main_path,"autogenarated_files","priority_list.txt"))
    if check_file == (False):
        open((os.path.join(main_path,"autogenarated_files","priority_list.txt")),"w").close()
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
    check_file = os.path.isfile(os.path.join(main_path,"autogenarated_files","quick_note.txt"))
    if check_file == (False):
        open((os.path.join(main_path,"autogenarated_files","quick_note.txt")),"w").close()
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

def roadmap():
    check_file = os.path.isfile(os.path.join(main_path,"autogenarated_files","roadmap.txt"))
    if check_file == (False):
        open((os.path.join(main_path,"autogenarated_files","roadmap.txt")),"w").close()
    with open((os.path.join(main_path,"autogenarated_files","roadmap.txt")),"r") as np_file:    
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
            os.startfile((os.path.join(main_path,"autogenarated_files","roadmap.txt")))
            break
        elif "*" in input0:
            replace_task = input0.replace("*"," ")
            with open((os.path.join(main_path,"autogenarated_files","roadmap.txt")),"a") as np_file:
                np_file.write(replace_task+ "\n")
                break
        elif input0 == ("read"):
            with open((os.path.join(main_path,"autogenarated_files","roadmap.txt")),"r") as np_file:
                print("")
                print(np_file.read())
        elif input0 == ("cls"):
            print("CLEAR THE ENTIRE CONTENT OF FILE..?")
            print("YES (Y) or NO (N)")
            confirmation = input_source.getkey()
            if confirmation == ("n") or confirmation == ("N"):
                roadmap()          
                break
            elif confirmation == ("y") or confirmation == ("Y"):
                file = open((os.path.join(main_path,"autogenarated_files","roadmap.txt")),"w")
                file.close()
                print("CLEARED THE CONTENT OF "+ '"'+"roadmap.txt"+'"')
            else:
                roadmap()
                break
        else:
            with open((os.path.join(main_path,"autogenarated_files","roadmap.txt")),"a") as np_file:
                np_file.write(input0+ "\n")

            