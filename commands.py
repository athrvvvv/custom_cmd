import random
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
"zoom","music","cmd command","priority list","github.com/athrvvvv","todo","documents", "pass", "quick note","jupyter notebook","clean bin","day","maximize","script","writer","vsdc","tracker","counter","bluetooth","BRAVE","BATTERY PERCENT","SIGNAL","CLICK","TELEGRAM","PHOTOS","WHATSAPP","CLOSE","TWITTER","TEMP","MESSAGES","CALENDAR","COMMANDS", "ZOOM", "RESTART","SLEEP","SHUTDOWN","YOUTUBE","WORD","GIMP", "FILES","PROJECTS","LISTW", "REOPEN","OPERA","TELEGRAM","PYTHON","TIME","DATE","ZOOM","MUSIC","CMD COMMAND","PRIORITY LIST", "TODO","DOCUMENTS", "PASS", "QUICK NOTE","JUPYTER NOTEBOOK","CLEAN BIN","DAY","MAXIMIZE","SCRIPT","VSDC","TRACKER","WRITER","COUNTER","BLUETOOTH"])

def commandss():
    data = [['KEY', 'USES'],
            ['REOPEN','REOPENS CUSTOM_CMD'],
            ['OPCMD','OPENS ANOTHER CUSTOM_CMD'],
            ['PS','PROJECT MANAGER'],
            ['CMD','CMD IN CUSTOM_CMD'],
            ['PYTHON','PYTHON IN CUSTOM_CMD'],
            ['LISTW','LIST OF WORD DOCUMENTS'],
            ['CLOSE','KILL OPERATONS'],
            ['PASS','STRONG PASSWORD GENERATOR'],
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

# TYPE IN HERE: 
list = ["GIVE CHARGE: ","GIVE CONTROL: ","COME TO POWER: ","ASSUME POWER: ","STEP IN: ","GIVE DIRECTION: ","GIVE COMMAND: ","STATE COMMAND: "]
choice_command = str(random.choice(list))
    