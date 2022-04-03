import os, readline
from datetime import datetime
import WConio2 as input_source
import docx, docx2txt
import commands
import WConio2 as IS
doc = docx.Document()

class MyCompleter(object):
    def __init__(self, options):
        self.options = sorted(options)
    def complete(self, text, state):
        if state == 0:  
            if text:
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:
                self.matches = self.options[:]
        try: 
            return self.matches[state]
        except IndexError:

            return None
            
readline.set_completer(commands.completer.complete)
readline.parse_and_bind('tab: complete')

#FUNCTION FOR CYCLE OF COMPLETER :)
def completer_on():
    readline.set_completer(commands.completer.complete)
    readline.parse_and_bind('tab: complete')

#LIST OF WORD DOCUMENTS
def listdir_word():
    filenames = os.listdir(r"C:\Users\athar\OneDrive\Documents\word_docs")
    print("")
    for filename in filenames:
        print(filename)
    print()
    completer = MyCompleter(filenames)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    print()
    ask_for_it = input("TYPE FILENAME: ")  
    print()
    if ask_for_it == ("r "+ask_for_it.replace("r ","")):
        my_text = docx2txt.process(r'C:/Users/athar/OneDrive/Documents/word_docs/' + ask_for_it.replace("r ",""))
        print(my_text)
        completer_on()
        exit
    elif ask_for_it == (""):
        print("C'mon")
        completer_on()
        print()
        exit
    
    elif ask_for_it == ("new"):
        print()
        input01 = input("ENTER FILENAME: ")
        print()
        #input02 = input("WANNA ADD HEADING: ")
        if input01 == (""):
            completer_on()
            print()
            StopIteration()
        else:
            filepath = (r"C:\Users\athar\OneDrive\Documents\word_docs/"+input01+".docx")
            #doc.add_heading(input02, 0)
            doc.save(filepath)
            print("OPEN (O) EXIT ()")
            option = IS.getkey()
            if option == ("o"):
                os.startfile(filepath)
                print()
            else:
                print()
                print("EXIT")
                print()
            completer_on()
        

    else:
        completer = MyCompleter(filenames)
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        input_path = (r'C:/Users/athar/OneDrive/Documents/word_docs/' + ask_for_it)
        check_file = os.path.isfile(input_path)
        if check_file == (True):
            os.startfile(input_path)
        else:
            print("FALSE FILE :(")
        completer_on()
       
#UI TO PY FILE CONVERSION
def ui_to_py():
    #cwd = os.getcwd()+"/OneDrive\Documents\projects\custom_cmd/"+"/frontend/"
    try:
        path, file_name = input("FILE PATH - FILE NAME:").split()
        os.system("pyuic5 -x "+'"'+path+"/"+file_name+".ui"+'"'+" -o "+'"'+path+"/"+file_name+".py"+'"')
    except:
        print("")
        print("Something went wrong :(")
        print()
        pass
    
#CREATE DUMMY PYTHON FILES
def dummy_file():
    now = datetime.now()
    space = " "
    current_time = now.strftime("%b_%d_%I.%M.%S")
    os.system("start"+"python >"+"C:/Users/athar/OneDrive/Documents/projects/dummy_folder/"+current_time+".py")
    os.popen('"'+"C:/Progra~1/Notepad++/notepad++.exe"+'"'+space+'"'+"C:/Users/athar/OneDrive/Documents/projects/dummy_folder/"+current_time+".py"+'"')
    
#DELETING THE CONTAIN INSIDE DUMMY DIR
def delete_dummy():
    os.system("del /S /Q C:\\Users\\athar\\OneDrive\\Documents\\projects\\dummy_folder")

#CREATING NEW DIR FROM CMD
def newfolder():
    try:
        where_folder, folder_name = input("LOCALITY-FOLDER: ").split()
        if where_folder == ("projects"):
            os.makedirs("C:/Users/athar/OneDrive/Documents/projects/"+folder_name)
            print("VS CODE OPEN (Y) SIMPLE OPEN (S) EXIT ()")
            print("")
            ask_for_opening = input_source.getkey()
            if ask_for_opening == ("s"):
                os.startfile("C:/Users/athar/OneDrive/Documents/projects/"+folder_name)
                exit
            if ask_for_opening == ("y"):
                os.system("code "+"C:/Users/athar/OneDrive/Documents/projects/"+folder_name)
                exit
            if ask_for_opening == (""):
                print("C'mon")
                exit
        if where_folder == ("desktop"):
            os.makedirs("C:/Users/athar/OneDrive/Desktop/"+folder_name)
            os.startfile("C:/Users/athar/OneDrive/Desktop/"+folder_name)
            
        if where_folder == ("download"):
            os.makedirs("C:/Users/athar/OneDrive/Download/"+folder_name)
            os.startfile("C:/Users/athar/OneDrive/Download/"+folder_name)

        if where_folder == ("document"):
            os.makedirs("C:/Users/athar/OneDrive/Documents/"+folder_name)
            os.startfile("C:/Users/athar/OneDrive/Documents/"+folder_name)
        
    except:
        pass
        print("")
        print("IT WAS STRANGE..!")
        print("")
    
#OPEINIG CERTAIN PROJECTS DIRECTLY IN VSCODE
def open_project_vs():
    path = (r"C:\Users\athar\OneDrive\Documents\projects")
    list = os.listdir(path)
    print()
    for filename in list:
        print(filename)
    print()
    completer = MyCompleter(list)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    input1 = input("FOLDER TO OPEN IN VS: ")
    if input1 == (""):
        completer_on()
        print()
        StopIteration
    elif (" np") in input1:
        folder_name_np = input1.replace(" np","")
        isdir = os.path.isdir(path+"/"+folder_name_np)
        if isdir == (True):
            folder_origin = (path +"/"+folder_name_np)
            list01 = os.listdir(folder_origin)
            for filename in list01:
                print(filename)
            print()
            completer = MyCompleter(list01)
            readline.set_completer(completer.complete)
            readline.parse_and_bind('tab: complete')
            filename_to_open = input("ENTER FILE TO OPEN: ")
            if filename_to_open == (""):
                print()
                StopIteration()   
            elif filename_to_open == ("f"):
                isdir = os.path.isdir(path+"/"+folder_name_np)
                if isdir == (True):
                    folder_origin = (path +"/"+folder_name_np)   
                    os.system("start notepad++ "+folder_origin)
                else:
                    print()
                    print("FALSE FILE NAME:(")
                    print()
                    completer_on() 
            else:
                check_file = os.path.isfile(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files\open_file_npp.txt")
                if check_file == (False):
                    os.system("echo> "+r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files\open_file_npp.txt")
                with open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files\open_file_npp.txt", 'w') as writer:
                    writer.write(" "+filename_to_open)
                with open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files\open_file_npp.txt", 'r') as writer:
                    number_of_files = 0
                    data = writer.read()
                    lines = data.split()
                    number_of_files += len(lines)
                    if number_of_files == (1):
                        print("1 FILE DETECTED")
                        input_path = (folder_origin +"/"+ filename_to_open)
                        check_file = os.path.isfile(input_path) 
                        if check_file == (True):
                            os.system("start notepad++ "+input_path)
                            print()
                            completer_on()
                            exit
                        else:
                            print()
                            print("FALSE FILE NAME:(")
                            print()
                            completer_on()                                         
                    else:
                        print(number_of_files,"FILES DETECTED")
                        with open (r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files\open_file_npp.txt", 'r') as replace_file:
                            slash = "/"
                            path = r"C:\Users\athar\OneDrive\Documents\projects"+slash+folder_name_np+slash
                            reading = replace_file.read()
                            replacing = reading.replace(" ",(" "+path))
                        with open (r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files\open_file_npp.txt", 'w') as write_file:
                            write_file.write(replacing)
                        data_in_file = open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenerated_files\open_file_npp.txt", 'r')
                        reading_data = data_in_file.read()
                        os.system("start notepad++ "+reading_data)
                        print()                                
        completer_on()       
    else:
        isdir = os.path.isdir(path+"/"+input1)
        completer_on()
        if isdir == (True):
            os.system("code "+path+"/"+input1)
            print()
            completer_on()
            exit
        else:
            print()
            print("FALSE FILE NAME:(")
            print()
            completer_on()
    
#JUPYTER NOTEBOOK
def jupyternotebook_ml_mf():
    os.startfile(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\jupyter_notebook.py")

#SUB-PROJECT SELECTER
def subproject():
    filenames = os.listdir(r"C:\Users\athar\OneDrive\Documents\projects")
    print("")
    for filename in filenames:
        print(filename)
    completer = MyCompleter(filenames)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    input1 = input("COMMAND: ")
    if ("clean ") in input1:
        temp = input1.replace("clean ","")
        a = (r"%userprofile%\OneDrive\Documents\projects\\"+temp+"\\")
        b = (r"C:\Users\athar\OneDrive\Documents\projects/"+temp)
        check_dir = os.path.isdir(b)
        if check_dir == (True):
            os.system("del "+a+"*.bak")
            #ADD VERIFICATION OF __pycache__
            os.system("del /s /q "+a+"__pycache__")
            os.system("rmdir "+a+"__pycache__")
            completer_on()
        else:
            print()
            print("FALSE DIR")
            print()
            completer_on()
    elif input1 == (""):
        os.system("start " r"C:\Users\athar\OneDrive\Documents\projects")
        completer_on()
    else:
        a = (r"C:\Users\athar\OneDrive\Documents\projects/"+input1)
        check_dir = os.path.isdir(a)
        if check_dir == (True):
            os.startfile(a)
            print()
            completer_on()
        else:
            print()
            print("FALSE DIR")
            print()
            completer_on()
    








    
