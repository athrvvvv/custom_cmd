import scheduler
import file_manangement
from clean_bin import clean_bin
from commands import commandss, introduction
from password_generator import password
from features01 import cmd_command, kill_task, ss, get_window_foreground, yt
from startfile import current_date, documents,open_resso,zoom,current_time, designer, npp, open_opera ,killandstartvs, ssf, open_telegram, code0,  open_cmd, open_current_in_cmd,  open_word_folder,dn_files, files, notepad,  pip, python, restart_terminal, shutdown, your_path, clear_console , restart, sleep1, whatsapp,word, gimp, edit,brave
from file_manangement import  dummy_file,jupyternotebook_ml_mf, listdir_word, newfolder, open_project_vs, ui_to_py
import readline
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
completer = MyCompleter(["brave", "telegram","commands", "zoom",
"restart","sleep","shutdown","youtube","word","gimp",
"files","projects","wd","listw",
"reopen","opera","telegram","python","time","date",
"new dir","zoom","kill","music","cmd command","priority list", "roadmap","documents", "pass", "quick note","jupyter notebook","clean bin"])
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

print("Let's make this capable..♥")
print("")
while True:
    while True: 
        val = input("TYPE COMMAND:")

        if val == ("cls"):
            clear_console()

        elif val == ("ss"):
            ss()
            
        elif val == ("exit"):
            exit()

        elif val == ("restart"):
            restart()

        elif val == ("sleep"): 
            sleep1() 

        elif val == ("bye") or val == ("shutdown"):
            shutdown()

        elif val == ("whatsapp"):
            print("FUNCTION HAS BEEN REMOVED")
        
        elif val == ("yt"):
            yt()

        elif val == ("word"):
            word()

        elif val == ("np"):
            notepad()
            
        elif val == ("gimp"):
            gimp()

        elif val == ("pdr"):
            edit()

        elif val == ("code"):
            code0() 

        elif val == ("brave"):
            brave()

        elif val == ("dn"):
            dn_files()

        elif val == ("files"):
            files()

        elif val == ("commands"):
            commandss()

        elif val == ("pip"):
            pip()

        elif val == ("wd"):
            open_word_folder()
        
        elif val == ("listw"):
            listdir_word()

        elif val == ("reopen"):
            restart_terminal()

        elif val == ("path"):
            your_path()

        elif val == ("opcmd"):
            open_current_in_cmd()

        elif val == ("cmd"):
            open_cmd()

        elif val == ("telegram"):
            open_telegram()
    
        elif val == ("rvs"):
            killandstartvs()

        elif val == ("opera"):
            open_opera()

        elif val == ("python"):
            python()
        
        elif val == ("vsp"):
            open_project_vs()
        
        elif val == ("time"):
            current_time()

        elif val == ("date"):
            current_date()
        
        elif val == ("qt"):
            designer()

        elif val == ("uic"):
            ui_to_py()
        
        elif val == ("nm"):
            dummy_file()
        
        elif val == ("npp"):
            npp()

        elif val == ("new dir"):
            newfolder()

        elif val == ("pass"):
            password()

        elif val == ("zoom"):
            zoom()

        elif val == ("kill"):
            kill_task()

        elif val == ("music"):
            open_resso()

        elif val == ("ssf"):
            ssf()

        elif val == ("fg"):
            get_window_foreground()
        
        elif val == ("cmd command"):
            cmd_command()
        
        elif val == ("priority list"):
            scheduler.priority_list()
        
        elif val == ("documents"):
            documents()
        
        elif val == ("quick note"):
            scheduler.quick_note()
        
        elif val == ("timer"):
            scheduler.tempo_timer()
        
        elif val == ("jupyter notebook"):
            jupyternotebook_ml_mf()
           
        elif val == ("clean bin"):
            clean_bin()

        elif val == ("roadmap"):
            scheduler.roadmap()
        
        elif val == ("babu"):
            introduction()
        
        elif val == ("ps"):
            file_manangement.subproject()
