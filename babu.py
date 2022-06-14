import time
timestamp12 = time.time()
import scheduler
import file_management
import cleaner
import commands
import password_generator
import features
import startfile
import gui_applications 
import os, readline, re

readline.set_completer(commands.completer.complete)
readline.parse_and_bind('tab: complete')
# All ESSENTIAL DIRS and FILES CHECKER
features.check_AppConfig()
# MAXIMISES PROGRAM 
features.maximize()
# GREETING
features.greet_time()
# LAST VISITED TIME
# FIX THE CONDITION
try: features.read_visited_time()
except: pass
# WRITING CURRENT TIME
features.write_time()
# REGISTER OPENING OF APP
features.visit_counter("count")
# Count greeting (For only one time a day)
features.greet()
# TELLING PRIORITY_LIST
scheduler.check_prio_status()
# TELLING TODO LIST
scheduler.check_todo_status()
features.write_empty("clear")
main_path = os.path.dirname(__file__)
timestamp22 = time.time()
print("Startup took %.2f seconds" % (timestamp22 - timestamp12))

while True:
    inp = input(commands.choice_command).lower()
    val=(re.compile(r'[^a-zA-Z-).]').sub(" ",inp)).strip()
    features.auto_bs_search(val)
    features.write_empty("check_count")
    if val == ("cls"):
        os.system("cls")
    
    elif val == ("exit"):
        os._exit(0)

    elif val == ("restart"):
        startfile.restart()

    elif val == ("sleep"): 
        startfile.sleep1() 

    elif val == ("bye") or val == ("shutdown"):
        features.write_time()
        startfile.shutdown()

    elif val == ("whatsapp"):    
        startfile.whatsapp()

    elif val == ("ytw"):
        features.yt()

    elif val == ("word"):
        startfile.word()

    elif val == ("np"):
        startfile.notepad()
        
    elif val == ("gimp"):
        startfile.gimp()

    elif val == ("pdr"):
        startfile.edit()

    elif val == ("code"):
        startfile.code0() 

    elif val == ("brave"):
        startfile.brave()

    elif val == ("dn"):
        startfile.dn_files()

    elif val == ("files"):
        startfile.files()

    elif val == ("commands"):
        commands.commandss()

    elif "pip " in val:
        startfile.pip(val)

    elif val == ("wd"):
        startfile.open_word_folder()
    
    elif val == ("listw"):
        file_management.listdir_word()

    elif val == ("reopen"):
        startfile.restart_terminal()

    elif val == ("opcmd"):
        startfile.open_current_in_cmd()

    elif val == ("cmd"):
        startfile.open_cmd()

    elif val == ("telegram"):
        startfile.open_telegram()

    elif val == ("rvs"):
        startfile.killandstartvs()

    elif val == ("python"):
        startfile.python()
    
    elif val == ("time"):
        features.current_time()

    elif val == ("date"):
        features.current_date()
    
    elif val == ("qt"):
        startfile.designer()

    elif val == ("uic"):
        gui_applications.ui_to_py()
    
    elif val == ("nm"):
        file_management.dummy_file()
    
    elif ("nm-") in val:
        temp = val.replace("nm-","")
        file_management.custom_dummy_file(temp)
    
    elif val == ("npp"):
        startfile.npp()

    elif val == ("pass"):
        password_generator.password()

    elif val == ("zoom"):
        startfile.zoom()

    elif val == ("close"):
        features.kill_task()

    elif val == ("music"):
        startfile.open_resso()

    elif val == ("ssf"):
        startfile.ssf()

    elif val == ("fg"):
        features.get_window_foreground()
    
    elif val == ("cmd command"):
        features.cmd_command()
    
    elif val == ("priority list"):
        scheduler.priority_list()
    
    elif val == ("documents"):
        startfile.documents()
    
    elif val == ("quick note"):
        scheduler.quick_note()
    
    elif val == ("clean bin"):
        cleaner.clean_bin()

    elif val == ("todo"):
        scheduler.todo()
    
    elif val == ("ps"):
        file_management.subproject(val.upper())
        
    elif val == ("yt"):
        startfile.youtubewa()
    
    elif val == ("photos"):
        startfile.googlephotos()
    
    elif val == ("calendar"):
        startfile.calendar()
    
    elif val == ("bin"):
        startfile.bin()
    
    elif val == ("messages"):
        startfile.messages()

    elif val == ("temp"):
        cleaner.clean_temp()
    
    elif val == ("fk"):
        print()
        password_generator.get_pass()
        print()
    
    elif val == ("twitter"):
        startfile.twitter()
    
    elif val == ("signal"):
        startfile.signal()
        
    elif val == ("ss"):
        os.startfile(os.path.join(main_path,"screenshot.pyw"))
    
    elif val == ("print"):
        startfile.print()

    elif val == ("battery percent"):
        features.battery_percent()
    
    elif val == (")"):
        print()
        print("Hello. Welcome.")
        print()
        
    elif val == ("k"):
        features.kill_selective_tasks()
    
    elif val == ("day"):
        features.current_day()
    
    elif val == ("maximize"):
        features.maximize()
    
    elif val == ("fdm"):
        startfile.fdm()
    
    elif ("bs") in val:
        main_bs = val.replace("bs","")
        features.brave_search(main_bs)
        
    elif val == ("vsdc"):
        startfile.vsdc()
        
    elif ".com" in val or ".be" in val or ".org" in val:
        features.com(val)
 
    elif "x" in val:
        try:
            answer = inp.replace("x","")
            ans = int(answer)
            features.refresh_x(ans)
        except:
            pass

    elif val == "writer":
        features.writer()
    
    elif val == "whatsappp":
        startfile.whatsapp_stable()

    elif val == ("nmf"):
        file_management.nmf() 
    
    elif ("bluetooth ") in val:
        temp = val.replace("bluetooth","")
        features.bluetooth(temp)
    
    elif val == ("timer"):
        os.startfile(os.path.join(main_path,"timer.pyw"))

    elif len(val) < 1:
        features.write_empty("write")
    
    elif ("prio-") in val:
        scheduler.set_on_off_prio(val)
    
    elif ("todo-") in val:
        scheduler.set_on_off_todo(val)
        
    elif val == ("mute"):
        features.mute_speakers()
    
    elif val == ("log"):
        features.visit_counter("log")
    
    elif ("wifi- ") in val:
        features.wifi(val)
    
    elif val == ("start ."):
        os.startfile(main_path)

    elif val == ("ec"): file_management.subproject(val.upper())

    elif val == ("js"): file_management.subproject(val.upper())
