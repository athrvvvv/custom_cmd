import os,winshell
def clean_bin():
    #os.system("rd /s /q %systemdrive%\$Recycle.bin")
    #WITH DUST
    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
    #NO DURST

def clean_temp():
    os.system("del /s /q "+r"C:\Users\athar\AppData\Local\Temp")

 