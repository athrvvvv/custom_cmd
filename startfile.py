import os, sys
from file_management import delete_dummy
import cleaner

def dn_files():
    os.startfile(r"C:\Users\athar\Downloads")

def project():
    os.startfile(r"C:\Users\athar\OneDrive\Documents\projects")

def zoom1():
    os.startfile("C:\\Users\\athar\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

def restart():
    os.system("shutdown /r /t 0")
    os.system("taskkill /im python.exe /f")
    os._exit(1)

def shutdown():
    delete_dummy()
    cleaner.clean_temp()
    os.system("shutdown /s /t 0")
    os._exit(1)

def sleep1():
    os.system("shutdown /h ") 
    
def whatsapp():
    os.system("start whatsapp://send?phone=")

def word():
    os.system("start winword")

def gimp():
    os.startfile("C:\\Users\\athar\\AppData\\Local\\Programs\\GIMP 2\\bin\\gimp-2.10.exe")

def edit():
    os.startfile("C:\\Program Files\\CyberLink\\PowerDirector19\\pdr.exe")

def code0():
    os.system("code")

def brave():
    os.system("start brave")

def clear_console():
    os.system('cls')

def pip():
    pip_work = input("")
    if "pip install" in pip_work:
        try:
            os.system(pip_work)
        except:
            pass
    elif pip_work == (""):
        StopIteration()
    else:
        try:
            internal_command = ("pip install " + pip_work)
            os.system(internal_command)
        except:
            pass

def files():
    os.system("explorer")

def notepad():
    os.system("start notepad")

def note_folder():
    os.startfile(r"C:\Users\athar\OneDrive\Documents\notes")

def open_word_folder():
    os.startfile(r"C:\Users\athar\OneDrive\Documents\word_docs")
    
def restart_terminal():
    os.system("start babu")
    sys.exit("BYEEEE")

def your_path():
    os.startfile(r"C:\Users\athar\OneDrive\Documents\projects\custom_cmd")

def open_current_in_cmd():
    os.system("start babu")

def open_cmd():
    os.system("cmd")

def open_telegram():
    os.startfile(r"C:\Users\athar\AppData\Roaming\Telegram Desktop\Telegram.exe")

def forcewhatsapp():
    os.startfile(r"C:\Users\athar\OneDrive\Documents\force\WhatsAppSetup.exe")

def killandstartvs():
    os.system("taskkill /im Code.exe /f")
    os.system("code")

def open_opera():
    os.system("start opera")

def python():
    os.system("python")


def designer():
    os.startfile(r"C:\Qt\6.1.2\mingw81_64\bin\designer.exe")

def npp():
    os.system("start notepad++")

def zoom():
    os.startfile(r"C:\Users\athar\OneDrive\Documents\projects\zoom_bot\main.py")

def open_resso():
    os.system(r" start C:\Users\athar\AppData\Local\Programs\Resso\Resso.exe")

def ssf():
    os.startfile(r"C:\Users\athar\OneDrive\Pictures\Screenshots")

def documents():
    os.system("start " +r"C:\Users\athar\OneDrive\Documents")

def googlephotos():
    os.system("explorer shell:appsfolder\Brave._crx_ncmjhecbjefahankockkkdmedg")

def youtubewa():
    os.system("explorer shell:appsfolder\Brave._crx_agimnkijcamfeangaknmldooml")

def calendar():
    os.system("explorer shell:appsfolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar")

def bin():
    os.system("explorer shell:appsFolder\::{645FF040-5081-101B-9F08-00AA002F954E}")

def messages():
    os.system("explorer shell:appsFolder\Brave._crx_hpfldicfbfkngkocigghgafkph")

def twitter():
    os.system("explorer shell:appsFolder\Brave._crx_jgeocpdicgpbanhokmhcgcflmi")

def signal():
    os.system("explorer shell:appsFolder\org.whispersystems.signal-desktop")

def print():   
    os.startfile(r"C:\Program Files\HP\HP Ink Tank Wireless 410 series\Bin\HP Ink Tank Wireless 410 series.exe")


