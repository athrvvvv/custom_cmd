import os, readline

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

# AUTOMATIING JUPYTER NOTEBOOK (ML FILES)
file_path = (r"C:\Users\athar\OneDrive\Documents\machine_learning")
filenames = os.listdir(file_path)
print("")
for filename in filenames:
    print(filename)
def completor_on():
    completer = MyCompleter(filenames)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')

def resuming_flow():
    input1 = input("FILE TO OPEN: ") 
    new_path = (file_path+"/"+input1)
    check_file = os.path.isdir(new_path)
    if check_file == (True):
        os.system("jupyter notebook "+new_path)
    else:
        print("FATAL ERROR.. :(")

input1 = input("FILE TO OPEN: ") 

if input1 == (""):
    exit()

if "mkdir " in input1:
    command = input1.replace("mkdir ","")
    try:
        os.system(r"mkdir C:\Users\athar\OneDrive\Documents\machine_learning"+"\\"+command)
        completor_on()
        resuming_flow()
    except:
        pass
        completor_on()
        resuming_flow()
else:
    new_path = (file_path+"/"+input1)
    check_file = os.path.isdir(new_path)
    if check_file == (True):
        os.system("jupyter notebook "+new_path)
    else:
        print("FATAL ERROR.. :(")

