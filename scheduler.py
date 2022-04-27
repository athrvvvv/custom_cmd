import os
import WConio2 as input_source
from datetime import date
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
            confirmation = input_source.getkey()
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
            confirmation = input_source.getkey()
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
            confirmation = input_source.getkey()
            if confirmation == ("n") or confirmation == (""):
                roadmap()
            
            else:
                file = open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\roadmap.txt","w")
                file.close()
                print("CLEARED THE CONTENT OF "+ '"'+"roadmap.txt"+'"')
        else:
            with open(r"C:\Users\athar\OneDrive\Documents\projects\hidden_works\roadmap.txt", "a") as np_file:
                np_file.write(input0+ "\n")

            