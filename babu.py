import scheduler
import file_management
import cleaner
import commands
import password_generator
import features
import startfile
import tracking_master  
import readline
import os, re, importlib

readline.set_completer(commands.completer.complete)
readline.parse_and_bind('tab: complete')
# MAXIMISES PROGRAM 
features.maximize()
# FUNCTIONALITY FOR blank inputs
features.clear_command_history()
# Count greeting (For only one time a day)
features.greet()
# All ESSENTIAL DIRS and FILES CHECKER
features.check_dir()
# FUNCTIONALITY FOR tracking master
tracking_master.count_on()

main_path = os.path.dirname(__file__)

while True: 
    # val01 = input("TYPE COMMAND:")
    val01 = input("TYPE IN HERE:")
    val = val01.lower().strip()
    features.check_empty_command()
    if val == ("cls"):
        startfile.clear_console()

    elif val == ("exit"):
        exit()

    elif val == ("restart"):
        startfile.restart()

    elif val == ("sleep"): 
        startfile.sleep1() 

    elif val == ("bye") or val == ("shutdown"):
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

    elif val == ("path"):
        startfile.your_path()

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
        file_management.ui_to_py()
    
    elif val == ("nm"):
        file_management.dummy_file()
    
    elif val == ("npp"):
        startfile.npp()

    elif val == ("new dir"):
        file_management.newfolder()

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
    
    elif val == ("cmdcommand"):
        features.cmd_command()
    
    elif val == ("prioritylist"):
        scheduler.priority_list()
    
    elif val == ("documents"):
        startfile.documents()
    
    elif val == ("quicknote"):
        scheduler.quick_note()
       
    elif val == ("cleanbin"):
        cleaner.clean_bin()

    elif val == ("roadmap"):
        scheduler.roadmap()
    
    elif val == ("ps"):
        file_management.subproject()
    
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
        features.get_pass()
        print()
    
    elif val == ("twitter"):
        startfile.twitter()
    
    elif val == ("signal"):
        startfile.signal()
        
    elif val == ("ss"):
        features.click()
     
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
    
    elif val == ("script"):
        startfile.script()
    
    elif val == ("fdm"):
        startfile.fdm()
    
    elif ("bs") in val:
        main_bs = val.replace("bs","")
        features.brave_search(main_bs)
        
    elif val == ("vsdc"):
        startfile.vsdc()
        
    elif ".com" in val or ".be" in val or ".org" in val:
        features.com(val)
    
    elif val == ("-status"):
        tracking_master.tracker_status()
    
    elif ("-status") in val :
        status = val.replace("-status","")
        if status == ('on') or status == ('off'):
            tracking_master.status_writer(status)
            print("Status updated")
        else:
            print("You can only set status to ON or OFF")
            StopIteration()
            
    elif val == ('tracker'):
        tracking_master.tracker()
    
    elif "x" in val:
        answer = val.replace("x","")
        ans = int(answer)
        features.refresh_x(ans)
    
    elif val == ("re"):
        importlib.reload(file_management)
        importlib.reload(scheduler)
        importlib.reload(commands)
        importlib.reload(password_generator)
        importlib.reload(features)
        importlib.reload(startfile)
        importlib.reload(tracking_master)
        importlib.reload(cleaner)

    elif "" in val:
        with open(os.path.join(main_path,'autogenerated_files','command_history.txt'),'a') as f:
            f.write("EMPTY"+"\n")