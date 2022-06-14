import os, json
import file_management, cleaner, features

main_path = (os.path.dirname(__file__))

def dn_files():
    os.system("start %userprofile%\Downloads")

def zoom():
    os.startfile("C:\\Users\\athar\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

def restart():
    os.system("shutdown /r /t 0")
    os.system("taskkill /im python.exe /f")
    os._exit(0)

def shutdown():
    file_management.delete_dummy()
    cleaner.clean_temp()
    features.visit_counter("count")
    os.system("shutdown /s /t 0")
    os._exit(0)

def sleep1():
    cleaner.clean_temp()  
    os.system("shutdown /h") 
    
def whatsapp():
    os.system("start whatsapp://send?phone=")

def word():
    os.system("start winword")

def gimp():
    os.startfile("C:\\Users\\athar\AppData\Local\Programs\GIMP 2\bin\gimp-2.10.exe")

def edit():
    os.startfile("C:\\Program Files\\CyberLink\\PowerDirector19\\pdr.exe")

def code0():
    os.system("code")

def brave():
    os.system("start brave")

def pip(self):
    try:
        os.system(self)
    except:
        pass

def files():
    os.system("explorer")

def notepad():
    os.system("start notepad")

def open_word_folder():
    with open ((os.path.join(main_path,"paths.json")),"r") as f:
        data1 = json.load(f)
        dir01 = data1["MSWORD"]
    os.startfile(dir01)

def open_cmd():
    os.system("cmd")

def open_telegram():
    os.startfile(r"C:\Users\athar\AppData\Roaming\Telegram Desktop\Telegram.exe")

def whatsapp_stable():
    os.system("explorer shell:appsFolder\com.squirrel.WhatsApp.WhatsApp")

def open_opera():
    os.system("start opera")

def python():
    os.system("python")

def designer():
    os.startfile(r"C:\Qt\6.1.2\mingw81_64\bin\designer.exe")

def npp():
    os.system("start notepad++")

def open_resso():
    os.system(r"start C:\Users\athar\AppData\Local\Programs\Resso\Resso.exe")

def ssf():
    os.startfile(r"C:\Users\athar\OneDrive\Pictures\Screenshots")

def googlephotos():
    os.system("explorer shell:appsFolder\Brave._crx_ncmjhecbjefahankockkkdmedg")

def youtubewa():
    os.system("explorer shell:appsFolder\Brave._crx_agimnkijcamfeangaknmldooml")

def calendar():
    os.system("explorer shell:appsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar")

def bin():
    os.system("start shell:RecycleBinFolder")

def messages():
    os.system("explorer shell:appsFolder\Brave._crx_hpfldicfbfkngkocigghgafkph")

def twitter():
    os.system("explorer shell:appsFolder\Brave._crx_jgeocpdicgpbanhokmhcgcflmi")

def signal():
    os.system("explorer shell:appsFolder\org.whispersystems.signal-desktop")

def print():   
    os.startfile(r"C:\Program Files\HP\HP Ink Tank Wireless 410 series\Bin\HP Ink Tank Wireless 410 series.exe")

def fdm():
    os.system("explorer shell:appsFolder\FreeDownloadManager")

def vsdc():
    os.system("explorer shell:appsFolder\{6D809377-6AF0-444B-8957-A3773F02200E}\FlashIntegro\VideoEditor\VideoEditor.exe")




