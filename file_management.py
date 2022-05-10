import os, readline
from datetime import datetime
import WConio2 as input_source
import docx, docx2txt
import commands
import tracking_master
import shutil
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

main_path = (os.path.dirname(__file__))

#FUNCTION FOR CYCLE OF COMPLETER :)
def completer_on():
    readline.set_completer(commands.completer.complete)
    readline.parse_and_bind('tab: complete')

#LIST OF WORD DOCUMENTS
def listdir_word():
    # Input from User
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
    elif ask_for_it == (""):
        os.system(r"start C:\Users\athar\OneDrive\Documents\word_docs")
    elif ask_for_it == ("new"):
        print()
        input01 = input("ENTER FILENAME: ")
        print()
        #input02 = input("WANNA ADD HEADING: ")
        if input01 == (""):
            print()
            StopIteration()
        else:
            filepath = (r"C:\Users\athar\OneDrive\Documents\word_docs/"+input01+".docx")
            #doc.add_heading(input02, 0)
            doc.save(filepath)
            print("OPEN (O) EXIT ()")
            option = input_source.getkey()
            if option == ("o"):
                os.startfile(filepath)
                print()
            else:
                print()
                print("EXIT")
                print()

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
    
#CREATE DUMMY PYTHON FILES
def dummy_file():
    now = datetime.now()
    space = " "
    current_time = now.strftime("%b_%d_%I.%M.%S")
    open(("C:/Users/athar/OneDrive/Documents/projects/dummy_folder/"+current_time+".py"),"w").close()
    os.popen('"'+"C:/Progra~1/Notepad++/notepad++.exe"+'"'+space+'"'+"C:/Users/athar/OneDrive/Documents/projects/dummy_folder/"+current_time+".py"+'"')

def custom_dummy_file(self):
    check_self = os.path.exists(os.path.join((main_path.replace("\custom_cmd","")),"imp_code",(self+".py")))
    if self == "":
        StopIteration()
    else:
        if check_self == (False):
            open(os.path.join(main_path.replace("\custom_cmd",""),"imp_code",(self+".py")),"w").close()
            os.popen("start notepad++ "+'"'+(os.path.join((main_path.replace("\custom_cmd","")),"imp_code",(self+".py")))+'"')
        else:
            print()
            print("FILE ALREADY EXISTS")
            print() 
            os.popen("start notepad++ "+'"'+(os.path.join((main_path.replace("\custom_cmd",""),"imp_code",(self+".py")))+'"'))
            
#DELETING THE CONTAIN INSIDE DUMMY DIR
def delete_dummy():
    path = (os.path.join((os.path.dirname(main_path)),"dummy_folder"))
    filenames = os.listdir(path)
    for filename in filenames:
        os.remove(os.path.join(path,filename))
        
#CREATING NEW DIR FROM CMD
def newfolder():
    try:
        where_folder, folder_name = input("LOCALITY-FOLDER: ").split()
        if where_folder == ("projects"):
            os.makedirs("C:/Users/athar/OneDrive/Documents/projects/"+folder_name)
            print("VS CODE OPEN (Y) SIMPLE OPEN (S) EXIT ()")
            print("")
            ask_for_opening = input_source.getkey()
            if ask_for_opening == ("s") or ask_for_opening == ("S"):
                os.startfile("C:/Users/athar/OneDrive/Documents/projects/"+folder_name)
                exit
            if ask_for_opening == ("y") or ask_for_opening == ("Y"):
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

#SUB-PROJECT SELECTER (PS FUNCTION)
def subproject():
    path = (r"C:\Users\athar\OneDrive\Documents\projects")
    filenames = os.listdir(path)
    print("")
    for filename in filenames:
        print(filename)
    print()
    completer = MyCompleter(filenames)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    input1 = input("FOLDER / FILE: ")
    if (" clean") in input1:
        dir_name = input1.replace(" clean","").strip()
        initial_path = os.path.join(path,dir_name)
        check_initial = os.path.exists(initial_path)
        if check_initial == (True):
            full_path = os.listdir(initial_path)
            check_cache = os.path.exists(os.path.join(path,dir_name,"__pycache__"))
            for f in full_path:
                if f.endswith(".bak"):
                    os.remove(os.path.join(initial_path,f))
            if check_cache == (True):
                shutil.rmtree(os.path.join(path,dir_name,"__pycache__"))
    elif input1 == (""):
        os.system("start " r"C:\Users\athar\OneDrive\Documents\projects")
    elif input1 == ("q"):
        StopIteration()
    # OPENS CMD IN SPECIFIC DIR
    elif " cmd" in input1:
        temp = input1.replace(" cmd","")
        b = (r"C:\Users\athar\OneDrive\Documents\projects/"+temp)
        check_file = os.path.exists(b)
        if check_file == (True):
            os.system("start cmd /K cd "+b)
        else:
            print()
            print("FALSE DIR")
            print()
    # OPENS GIT IN SPECIFIC DIR
    elif " git" in input1:
        temp = input1.replace(" git","")
        b = (r"C:\Users\athar\OneDrive\Documents\projects/"+temp)
        check_file = os.path.exists(b)
        if check_file == (True):
            os.popen(('"'+"C:\Program Files\Git\git-bash.exe"+'" '+"--cd="+'"'+b+'"'))
        else:
            print()
            print("FALSE DIR")
            print()
    # OPEN FOLDERS IN VS CODE
    elif " vs" in input1:
        temp = input1.replace(" vs","")
        isdir = os.path.isdir(path+"/"+temp)
        if isdir == (True):
            os.system("code "+path+"/"+temp)
            print()
            StopIteration()
        elif isdir == (False):
            print()
            print("FALSE FILE NAME:(")
            print()
    # OPEN PARTICULAR FILES IN VS CODE
    elif " -vs" in input1:
        folder_name_vs = input1.replace(" -vs","")
        isdir = os.path.isdir(path+"/"+folder_name_vs)
        if isdir == (True):
            folder_origin = (path +"/"+folder_name_vs)
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
            elif filename_to_open == ("new"):
                new_file = input("FILE NEW FILE NAME: ")
                if new_file == (""):
                    StopIteration()
                else:
                    path_of_file = (path+"/"+folder_name_vs+"/"+new_file+".py")
                    check_file_exists = os.path.exists(path_of_file)
                    if check_file_exists == (False):
                        os.system("echo "+'"'+"Happy Coding :)"+'"'+">>" +path_of_file)
                        print("OPEN (O) EXIT ()")
                        to_do = input_source.getkey()
                        if to_do == ("o"):
                            os.system("start code "+path_of_file)
                        else:
                            StopIteration()
                    elif check_file_exists == (True):
                        print()
                        print("FILE ALREADY EXISTS")  
                        print()    
            else:
                check_file = os.path.isfile(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_vs.txt")
                if check_file == (False):
                    os.system("echo> "+r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_vs.txt")
                with open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_vs.txt", 'w') as writer:
                    writer.write(" "+filename_to_open)
                with open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_vs.txt", 'r') as writer:
                    number_of_files = 0
                    data = writer.read()
                    lines = data.split()
                    number_of_files += len(lines)
                    if number_of_files == (1):
                        input_path = (folder_origin +"/"+ filename_to_open)
                        check_file = os.path.isfile(input_path) 
                        if check_file == (True):
                            print("1 FILE DETECTED")
                            os.system("code "+input_path)
                            print()
                            exit
                        else:
                            print()
                            print("FALSE FILE NAME:(")
                            print()                                      
                    else:
                        print(number_of_files,"FILES DETECTED")
                        with open (r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_vs.txt", 'r') as replace_file:
                            slash = "/"
                            path = r"C:\Users\athar\OneDrive\Documents\projects"+slash+folder_name_vs+slash
                            reading = replace_file.read()
                            replacing = reading.replace(" ",(" "+path))
                        with open (r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_vs.txt", 'w') as write_file:
                            write_file.write(replacing)
                        data_in_file = open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_vs.txt", 'r')
                        reading_data = data_in_file.read()
                        os.system("code "+reading_data)
                        print()                                
    # Track projects shortcut
    elif (" -track") in input1:
        to_track = input1.replace(' -track','')
        check_to_track = os.path.exists(os.path.join(path,to_track))
        if check_to_track == (False):
            print(os.path.join(path,to_track) + 'is FALSE DIR')
        else:
            input_to_tarck = open(os.path.join(main_path,'tracker','track_on.txt'),'w')
            input_to_tarck.write(to_track+'.txt')
            tracking_master.count_on()
    # OPENS ANY FILES/DIR IN NPP 
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
            elif filename_to_open == ("new"):
                new_file = input("FILE NEW FILE NAME: ")
                if new_file == (""):
                    StopIteration()
                else:
                    path_of_file = (path+"/"+folder_name_np+"/"+new_file+".py")
                    check_file_exists = os.path.exists(path_of_file)
                    if check_file_exists == (False):
                        os.system("echo "+'"'+"Happy Coding :)"+'"'+">>" +path_of_file)
                        print("OPEN (O) EXIT ()")
                        to_do = input_source.getkey()
                        if to_do == ("o"):
                            os.system("start notepad++ "+path_of_file)
                        else:
                            StopIteration()
                    elif check_file_exists == (True):
                        print()
                        print("FILE ALREADY EXISTS")      
                        print()
            else:
                with open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_npp.txt", 'w') as writer:
                    writer.write(" "+filename_to_open)
                with open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_npp.txt", 'r') as writer:
                    number_of_files = 0
                    data = writer.read()
                    lines = data.split()
                    number_of_files += len(lines)
                    if number_of_files == (1):
                        input_path = (folder_origin +"/"+ filename_to_open)
                        check_file = os.path.isfile(input_path) 
                        if check_file == (True):
                            print("1 FILE DETECTED")
                            os.system("start notepad++ "+input_path)
                            print()
                        else:
                            print()
                            print("FALSE FILE NAME:(")
                            print()                                         
                    else:
                        print(number_of_files,"FILES DETECTED")
                        with open (r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_npp.txt", 'r') as replace_file:
                            slash = "/"
                            path = r"C:\Users\athar\OneDrive\Documents\projects"+slash+folder_name_np+slash
                            reading = replace_file.read()
                            replacing = reading.replace(" ",(" "+path))
                        with open (r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_npp.txt", 'w') as write_file:
                            write_file.write(replacing)
                        data_in_file = open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_npp.txt", 'r')
                        reading_data = data_in_file.read().split()
                        for word in reading_data:
                            is_file = os.path.exists(word)
                            if is_file == (True):
                                os.system("start notepad++ "+word)
                            else:
                                print("IGNORED SOME PSEUDO FILES")
                        print()                                 
    elif " bf" in input1:
        dir_name = input1.replace(" bf","")
        check_bf = os.path.exists(os.path.join(path,dir_name,"bugs&features.docx"))
        if check_bf == (True): 
            os.startfile(os.path.join(path,dir_name,"bugs&features.docx"))
        else:
            print()
            print("FILE DOES'NT EXISTS")
            shutil.copyfile((os.path.join(main_path,"autogenarated_files","bugs&features.docx")),(os.path.join(path,dir_name,"bugs&features.docx")))
            print()           
            print("CREATED NEW FILE : bugs&features.docx")
            print() 
            os.startfile(os.path.join(path,dir_name,"bugs&features.docx"))
    else:
        a = (r"C:\Users\athar\OneDrive\Documents\projects/"+input1)
        check_dir = os.path.isdir(a)
        if check_dir == (True):
            os.startfile(a)
            print()
        else:
            print()
            print("FALSE DIR")
            print()
    completer_on()

def nmf():
    project = r"C:\Users\athar\OneDrive\Documents\projects\imp_code"
    c = os.listdir(project)
    for f in c:
        if f.endswith(".bak"):
            os.remove(os.path.join(project,f))
    a = os.listdir(project)
    completer = MyCompleter(a)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    print()
    for file in a:
        if file.endswith(".py"):
            print(file)
    print()
    input1 = input("FILENAME TO OPEN: ")
    if input1 == (""):
        os.startfile(project)
    elif input1 == ("q"):
        StopIteration()
    else:
        checkfile = os.path.exists(os.path.join(project,input1))
        with open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_npp.txt", 'w') as writer:
            writer.write(" "+input1)
        with open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_npp.txt", 'r') as writer:
            number_of_files = 0
            data = writer.read()
            lines = data.split()
            number_of_files += len(lines)
            if number_of_files == (1):
                input_path = (os.path.join(project,input1))
                check_file = os.path.isfile(input_path) 
                if check_file == (True):
                    print("1 FILE DETECTED")
                    os.system("start notepad++ "+input_path)
                    print()
                else:
                    print()
                    print("FALSE FILE NAME:(")
                    print()                                        
            else:
                print(number_of_files,"FILES DETECTED")
                with open (r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_npp.txt", 'r') as replace_file:
                    slash = "/"
                    reading = replace_file.read()
                    replacing = reading.replace(" ",(" "+project+"/"))
                with open (r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_npp.txt", 'w') as write_file:
                    write_file.write(replacing)
                data_in_file = open(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd\autogenarated_files\open_file_npp.txt", 'r')
                reading_data = data_in_file.read().split()
                for word in reading_data:
                    is_file = os.path.exists(word)
                    if is_file == (True):
                        os.system("start notepad++ "+word)
                    else:
                        print("IGNORED SOME PSEUDO FILES")
                print()                                
    completer_on()    