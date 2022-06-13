import os, readline, json
from datetime import datetime
import WConio2 as input_source
import docx, docx2txt
import commands, features
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
    try: 
        with open ((os.path.join(main_path,"paths.json")),"r") as f:
            data1 = json.load(f)
            dir01 = data1["MSWORD"]
    except:
        print("FIRST-TIME WRITING WORD-PATH")
        with open ((os.path.join(main_path,"paths.json")),"r") as f:
            data = json.load(f)
        change = {"MSWORD":None}
        data.update(change)
        with open((os.path.join(main_path,"paths.json")),"a") as f:
            g = open((os.path.join(main_path,"paths.json")),"r+")
            g.truncate(0)
            json.dump(data,f,indent=4)
            print("END")
    with open ((os.path.join(main_path,"paths.json")),"r") as f:
            data1 = json.load(f)
            dir01 = data1["MSWORD"]
    if dir01 == (None):
        while True:
            inp = input("PASTE YOUR WORD DOCUMENT FOLDER PATH: ")
            check_dir = os.path.exists(inp)
            if check_dir == (True):
                change = {"MSWORD":inp}
                data.update(change)
                with open((os.path.join(main_path,"paths.json")),"a") as f:
                    g = open((os.path.join(main_path,"paths.json")),"r+")
                    g.truncate(0)
                    json.dump(data,f,indent=4)
                    print()
                    print("This function is made for management of Word documents.")
                    print("Enter a "+'"'+"?"+'" '+"mark to know particular documentation of this function.")
                    print()
                    break
            else:
                print("DIR DOES'NT EXISTS :)")
    with open ((os.path.join(main_path,"paths.json")),"r") as f:
        data = json.load(f)
        dir = data["MSWORD"]
    filenames = os.listdir(dir)
    print("")
    for filename in filenames:
        print(filename)
    print()
    completer = MyCompleter(filenames)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    print()
    ask_for_it = input("TYPE FILENAME: ").lower() 
    print()
    if ask_for_it == ("r "+ask_for_it.replace("r ","")):
        my_text = docx2txt.process(dir+ ask_for_it.replace("r ",""))
        print(my_text)
    elif ask_for_it == (""):
        os.startfile(dir)
    elif ask_for_it == ("?"):
        print("Documentation")
    elif ask_for_it == ("q"):
        StopIteration()
    elif ask_for_it == ("new"):
        print()
        input01 = input("ENTER FILENAME: ")
        print()
        if input01 == (""):
            print()
            StopIteration()
        else:
            filepath = (os.path.join(dir,(input01+".docx")))
            doc.save(filepath)
            print("OPEN (O) EXIT ()")
            optionn = input_source.getkey()
            option = optionn.lower()
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
        input_path = (os.path.join(dir,ask_for_it))
        check_file = os.path.isfile(input_path)
        if check_file == (True):
            os.startfile(input_path)
        else:
            print("FALSE FILE :(")
    completer_on()
    
#CREATE DUMMY PYTHON FILES
def dummy_file():
    dir_name = os.path.join(os.path.dirname(main_path),"dummy_folder")
    now = datetime.now()
    current_time = now.strftime("%b_%d_%I.%M.%S")
    open(os.path.join(dir_name,(current_time+".py")),"w").close()
    os.popen("start notepad++ "+'"'+(os.path.join(dir_name,(current_time+".py")))+'"')

#CREATE DUMMY CUSTOMIZE PYTHON FILES 
def custom_dummy_file(self):
    if ".pyw" in self:
        extension = (self+'.pyw')  
    else:
        extension = (self+'.py')
    outside_path = os.path.dirname(main_path)  
    file = (os.path.join(outside_path,'imp_code',extension))
    check_self = os.path.exists(file)
    if self == "":
        StopIteration()
    else:
        if check_self == (False):
            open(file,"w").close()
            os.popen("start notepad++ "+'"'+file+'"')
        else:
            print()
            print("FILE ALREADY EXISTS")
            print() 
            os.popen("start notepad++ "+'"'+file+'"')
            
#DELETING THE CONTAIN INSIDE DUMMY DIR
def delete_dummy():
    path = (os.path.join((os.path.dirname(main_path)),"dummy_folder"))
    filenames = os.listdir(path)
    for filename in filenames:
        os.remove(os.path.join(path,filename))
        
#SUB-PROJECT SELECTER (PS FUNCTION)
def subproject(self):
    try: 
        with open ((os.path.join(main_path,"paths.json")),"r") as f:
            data1 = json.load(f)
            dir01 = data1[(self+"_PATH")]
    except:
        print("FIRST-TIME WRITING {}-PATH".format(self))
        with open ((os.path.join(main_path,"paths.json")),"r") as f:
            data = json.load(f)
        change = {(self+"_PATH"):None}
        data.update(change)
        with open((os.path.join(main_path,"paths.json")),"a") as f:
            g = open((os.path.join(main_path,"paths.json")),"r+")
            g.truncate(0)
            json.dump(data,f,indent=4)
    with open ((os.path.join(main_path,"paths.json")),"r") as f:
            data1 = json.load(f)
            dir01 = data1[(self+"_PATH")]
    if dir01 == (None):
        while True:
            inp = input("PASTE YOUR PYTHON-PROJECT FOLDER PATH: ")
            check_dir = os.path.exists(inp)
            if check_dir == (True):
                change = {(self+"_PATH"):inp}
                data1.update(change)
                with open((os.path.join(main_path,"paths.json")),"a") as f:
                    g = open((os.path.join(main_path,"paths.json")),"r+")
                    g.truncate(0)
                    json.dump(data1,f,indent=4)
                    print()
                    print("This function is made for management of working Python project DIR management. Enhance your productivity with this :)")
                    print("Enter a "+'"'+"?"+'" '+"mark to know particular documentation of this function.")
                    print()
                    break
            else:
                print("DIR DOES'NT EXISTS :)")
    with open ((os.path.join(main_path,"paths.json")),"r") as f:
        data = json.load(f)
        path_file_in_json = data[(self+"_PATH")]
    filenames = os.listdir(path_file_in_json)
    print("")
    for filename in filenames:
        print(filename)
    print()
    completer = MyCompleter(filenames)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    input1 = input("FOLDER / COMMAND: ").lower()
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
        os.system("start "+path_file_in_json)
    elif input1 == ("q"):
        StopIteration()
    elif input1 == ("new profile"):
        profile_name = input("ENTER PROFILE SHORTCUT (For ex. PS,EC,OK): ").upper()
        with open ((os.path.join(main_path,"paths.json")),"r") as f:
            data = json.load(f)
        change = {(profile_name+"_PATH"):None}
        data.update(change)
        with open((os.path.join(main_path,"paths.json")),"a") as f:
            g = open((os.path.join(main_path,"paths.json")),"r+")
            g.truncate(0)
            json.dump(data,f,indent=4)
        with open((os.path.join(main_path,"babu.py")),"a") as f:
            f.write('\n'+"    elif val == ({}): file_management.subproject(val.upper())".format('"'+profile_name.lower()+'"')+'\n')
            print("REOPEN PROGRAM TO APPEND CHANGES")
    # OPENS CMD IN SPECIFIC DIR
    elif " cmd" in input1:
        temp = input1.replace(" cmd","")
        b = (os.path.join(path_file_in_json,temp))
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
        b = (os.path.join(path_file_in_json,temp))
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
        isdir = os.path.isdir(path_file_in_json+"/"+temp)
        if isdir == (True):
            os.system("code "+path_file_in_json+"/"+temp)
            print()
            StopIteration()
        elif isdir == (False):
            print()
            print("FALSE FILE NAME:(")
            print()
    # OPEN PARTICULAR FILES IN VS CODE
    elif " -vs" in input1:
        folder_name_vs = input1.replace(" -vs","")
        isdir = os.path.isdir(path_file_in_json+"/"+folder_name_vs)
        if isdir == (True):
            folder_origin = (path_file_in_json +"/"+folder_name_vs)
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
            elif "del " in filename_to_open:
                temp = filename_to_open.replace("del ","")
                b = (os.path.join(path_file_in_json,folder_name_vs,temp))
                check_file = os.path.exists(b)
                if check_file == (True):
                    os.remove(b)
                else:
                    print()
                    print("FALSE FILE")
                    print()
            elif filename_to_open == ("new"):
                new_file = input("FILE NEW FILE NAME: ")
                if new_file == (""):
                    StopIteration()
                else:
                    path_of_file = (os.path.join(path_file_in_json,folder_name_vs,(new_file+".py")))
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
                with open((os.path.join(main_path,"autogenarated_files","open_file_npp.txt")), 'w') as writer:
                    writer.write(" "+filename_to_open)
                with open((os.path.join(main_path,"autogenarated_files","open_file_npp.txt")), 'r') as writer:
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
                        with open ((os.path.join(main_path,"autogenarated_files","open_file_npp.txt")), 'w') as f:
                            path = os.path.join(path_file_in_json,folder_name_vs,filename_to_open)
                            f.write(path)
                        with open ((os.path.join(main_path,"autogenarated_files","open_file_npp.txt")), 'r') as f:
                            reading = f.read()
                            replace_things = reading.replace(" ",(" "+(os.path.join(path_file_in_json,folder_name_vs)+"/")))
                        with open ((os.path.join(main_path,'autogenarated_files','open_file_npp.txt')), 'w') as write_file:
                            write_file.write(replace_things)
                        data_in_file = open((os.path.join(main_path,'autogenarated_files','open_file_npp.txt')), 'r')
                        reading_data = data_in_file.read().split()
                        count = 0
                        for word in reading_data:
                            is_file = os.path.exists(word)
                            if is_file == (True):
                                os.system("code "+word)
                            elif is_file == (False):
                                count = count + 1
                                print_or_not = (True)
                        try:
                            if print_or_not == (True):
                                print("IGNORED {} PSEUDO FILES".format(count))
                            print()        
                        except: pass                                                           
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
        isdir = os.path.isdir(path_file_in_json+"/"+folder_name_np)
        if isdir == (True):
            folder_origin = (path_file_in_json+"/"+folder_name_np)
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
            elif "del " in filename_to_open:
                temp = filename_to_open.replace("del ","")
                b = (os.path.join(path_file_in_json,"custom_cmd",temp))
                check_file = os.path.exists(b)
                if check_file == (True):
                    os.remove(b)
                else:
                    print()
                    print("FALSE FILE")
                    print()   
            elif filename_to_open == ("f"):
                isdir = os.path.isdir(os.path.join(path_file_in_json,folder_name_np))
                if isdir == (True):
                    folder_origin = (os.path.join(path_file_in_json,folder_name_np)) 
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
                    path_of_file = (os.path.join(path,folder_name_np,(new_file+".py")))
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
                with open((os.path.join(main_path,"autogenarated_files","open_file_npp.txt")), 'w') as writer:
                    writer.write(" "+filename_to_open.strip())
                with open((os.path.join(main_path,"autogenarated_files","open_file_npp.txt")), 'r') as writer:
                    number_of_files = 0
                    data = writer.read()
                    lines = data.split()
                    number_of_files += len(lines)
                    if number_of_files == (1):
                        input_path = (os.path.join(folder_origin,filename_to_open))
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
                        with open ((os.path.join(main_path,"autogenarated_files","open_file_npp.txt")), 'w') as f:
                            path = os.path.join(path_file_in_json,folder_name_np,filename_to_open)
                            f.write(path)
                        with open ((os.path.join(main_path,"autogenarated_files","open_file_npp.txt")), 'r') as f:
                            reading = f.read()
                            replace_things = reading.replace(" ",(" "+(os.path.join(path_file_in_json,folder_name_np)+"/")))
                        with open ((os.path.join(main_path,'autogenarated_files','open_file_npp.txt')), 'w') as write_file:
                            write_file.write(replace_things)
                        data_in_file = open((os.path.join(main_path,'autogenarated_files','open_file_npp.txt')), 'r')
                        reading_data = data_in_file.read().split()
                        count = 0
                        for word in reading_data:
                            is_file = os.path.exists(word)
                            if is_file == (True):
                                os.system("start notepad++ "+word)
                            elif is_file == (False):
                                count = count + 1
                                print_or_not = (True)
                        try:
                            if print_or_not == (True):
                                print("IGNORED {} PSEUDO FILES".format(count))
                            print()        
                        except: pass                               
    elif " bf" in input1:
        input_no_spaces = ("".join(input1.split(" ")))
        dir_name = input_no_spaces.replace("bf","")
        check_bf = os.path.exists(os.path.join(path_file_in_json,dir_name,"bugs&features.docx"))
        if check_bf == (True): 
            os.startfile(os.path.join(path_file_in_json,dir_name,"bugs&features.docx"))
        else:
            print()
            print("FILE DOES'NT EXISTS")
            shutil.copyfile((os.path.join(main_path,"autogenarated_files","bugs&features.docx")),(os.path.join(path_file_in_json,dir_name,"bugs&features.docx")))
            print()           
            print("CREATED NEW FILE : bugs&features.docx")
            print() 
            os.startfile(os.path.join(path_file_in_json,dir_name,"bugs&features.docx"))
    else:
        a = (os.path.join(path_file_in_json,input1))
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
    outside_path = os.path.dirname(main_path)
    project = (os.path.join(outside_path,'imp_code'))
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
    input1 = input("FILENAME TO OPEN: ")
    if input1 == (""):
        os.startfile(project)
    elif input1 == ("q"):
        StopIteration()
    elif "del " in input1:
        temp = input1.replace("del ","")
        b = (os.path.join(project,temp))
        check_file = os.path.exists(b)
        if check_file == (True):
            os.remove(b)
        else:
            print()
            print("FALSE FILE")
            print()
    else:
        with open((os.path.join(main_path,'autogenarated_files','open_file_npp.txt')), 'w') as writer:
            writer.write(" "+input1.strip())
        with open((os.path.join(main_path,'autogenarated_files','open_file_npp.txt')), 'r') as writer:
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
                with open ((os.path.join(main_path,'autogenarated_files','open_file_npp.txt')), 'r') as replace_file:
                    reading = replace_file.read()
                    replacing = reading.replace(" ",(" "+project+"/"))
                with open ((os.path.join(main_path,'autogenarated_files','open_file_npp.txt')), 'w') as write_file:
                    write_file.write(replacing)
                data_in_file = open((os.path.join(main_path,'autogenarated_files','open_file_npp.txt')), 'r')
                reading_data = data_in_file.read().split()
                count = 0
                for word in reading_data:
                    is_file = os.path.exists(word)
                    if is_file == (True):
                        os.system("start notepad++ "+word)
                    elif is_file == (False):
                        count = count + 1
                        print_or_not = (True)
                try:
                    if print_or_not == (True):
                        print("IGNORED {} PSEUDO FILES".format(count))
                    print()        
                except: pass                               
    completer_on()    