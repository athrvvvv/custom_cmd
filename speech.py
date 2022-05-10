import pyttsx3
import speech_recognition as sr
import commands
import cleaner
import scheduler

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"You said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
    
    
import password_generator
import features
import startfile
import file_management
import tracking_master  
import os

features.maximize()
# Count greeting (For only one time a day)
features.greet()
# All ESSENTIAL DIRS and FILES CHECKER
features.check_dir()
# FUNCTIONALITY FOR tracking master
tracking_master.count_on()

main_path = os.path.dirname(__file__)

while True: 
    val = takeCommand().lower()

    if val == ("ss"):
        features.ss()
        
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

    elif val == ("youtube web"):
        features.yt()

    elif val == ("MS word"):
        startfile.word()

    elif val == ("notepad"):
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

    elif val == ("opera"):
        startfile.open_opera()

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

    elif "close" in val:
        import os
        os.system("TASKKILL /f /im "+val.replace("close","")+".exe")
        speak("Closing "+val.replace("close",""))

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
    
    elif val == ("timer"):
        scheduler.tempo_timer()
    
    elif val == ("jupyter notebook"):
        file_management.jupyternotebook_ml_mf()
        
    elif val == ("clean bin"):
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
        
    elif val == ("screenshot"):
        features.click()
     
    elif val == ("print"):
        startfile.print()

    elif val == ("battery percent"):
        features.battery_percent()
            
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
    
    elif (" bs") in val:
        main_bs = val.replace(" bs","")
        with open(os.path.join(main_path,'autogenarated_files','search.txt'), 'w') as f:
            f.write(main_bs)
            features.brave_search()
    
    elif " os" in val:
        main_os = val.replace(" os","")
        with open(os.path.join(main_path,'autogenarated_files','search.txt'), 'w') as f:
            f.write(main_os)        
            features.opera_search()
        
    elif val == ("vsdc"):
        startfile.vsdc()
            
    elif val == ("-status"):
        tracking_master.tracker_status()
    
    elif ("-status ") in val :
        status = val.replace("-status ","")
        if status == ('on') or status == ('off'):
            tracking_master.status_writer(status)
            print("Status updated")
        else:
            print("You can only set status to ON or OFF")
            StopIteration()
            
    elif val == ('tracker'):
        tracking_master.tracker()
