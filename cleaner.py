import os,winshell, shutil

def clean_bin():
    #os.system("rd /s /q %systemdrive%\$Recycle.bin")
    #WITH DUST
    try: winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
    except: pass
    #NO DURST

def clean_temp():
    # filenames = os.listdir(os.path.join(os.path.expanduser('~'),"AppData\Local\Temp"))
    # for filename in filenames:
    shutil.rmtree((os.path.join(os.path.expanduser('~'),"AppData\Local\Temp")),ignore_errors=True)
    # os.remove(os.path.join(os.path.expanduser('~'),"AppData\Local\Temp"))
    # os.system("del /s /q "+r"%userprofile%\AppData\Local\Temp")
    