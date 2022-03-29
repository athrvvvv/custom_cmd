import os, time

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

completer = MyCompleter(["brave","battery percent","signal","click","telegram","photos","whatsapp","close","twitter","temp","messages","calendar","commands", "zoom",
"restart","sleep","shutdown","youtube","word","gimp",
"files","projects","listw",
"reopen","opera","telegram","python","time","date",
"new dir","zoom","music","cmd command","priority list", "roadmap","documents", "pass", "quick note","jupyter notebook","clean bin","day","maximize","script","BRAVE","BATTERY PERCENT","SIGNAL","CLICK","TELEGRAM","PHOTOS","WHATSAPP","CLOSE","TWITTER","TEMP","MESSAGES","CALENDAR","COMMANDS", "ZOOM", "RESTART","SLEEP","SHUTDOWN","YOUTUBE","WORD","GIMP", "FILES","PROJECTS","LISTW", "REOPEN","OPERA","TELEGRAM","PYTHON","TIME","DATE", "NEW DIR","ZOOM","MUSIC","CMD COMMAND","PRIORITY LIST", "ROADMAP","DOCUMENTS", "PASS", "QUICK NOTE","JUPYTER NOTEBOOK","CLEAN BIN","DAY","MAXIMIZE","SCRIPT"])

def commandss():
    data = [['KEY', 'USES'],
            ['REOPEN','REOPENS CUSTOM_CMD'],
            ['OPCMD','OPENS ANOTHER CUSTOM_CMD'],
            ['VSP','OPEN FOLDER IN VSCODE'],
            ['CMD','CMD IN CUSTOM_CMD'],
            ['PYTHON','PYTHON IN CUSTOM_CMD'],
            ['LISTW','LIST OF .DOCX'],
            ['PIP','INSTALL PY-PACKAGES'],
            ['TASKKILL','KILL OPERATONS'],
            ['PASSWORD','STRONG PASSWORD GENERATOR'],
            ['ZOOM','ZOOM AUTOMATION'],
            ['NM','TEMPORARY PYTHON FILE'],
            ['UIC','UI TO PY CONVERTER'],
            
            ]
    dash = '-' * 30
    for i in range(len(data)):
        
        if i == 0:
            print(dash)
            print('{:<10s}{:^15s}'.format(data[i][0],data[i][1]))
            print(dash)
        else:
            print('{:<10s}{:^12s}'.format(data[i][0],data[i][1]))


# print("Upcoming Ultra Super Powerful Artificial Intelligence.")


