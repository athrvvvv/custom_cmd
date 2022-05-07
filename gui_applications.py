import PySimpleGUI as sg
import os
main_path = (os.path.dirname(__file__))
def ui_to_py():     
    sg.theme('Dark Grey 13')
    event, values  = sg.Window('UIC CONVERTER', [[sg.Text('Select File To Convert')],
                            [sg.InputText(), sg.FileBrowse()],
                            [sg.Button("Okay"), sg.Cancel()]]).read(close=True)
    source_filename = values[0]
    check_file = os.path.exists(source_filename)
    if check_file == (True):
        os.system("pyuic5 -x "+'"'+source_filename+'"'+" -o "+'"'+(source_filename.replace(".ui",""))+".py"+'"')
        dir = os.path.dirname(source_filename)
        os.startfile(dir)
    else:
        print("FILE DOES'NT EXISTS")
