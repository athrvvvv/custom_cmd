import readline
import commands
import os
from datetime import date, timedelta

main_path = (os.path.dirname(__file__))

#This is for AutoComplete on clicking "TAB"
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
            
def completer_on():
    readline.set_completer(commands.completer.complete)
    readline.parse_and_bind('tab: complete')

# See the status (of tracker)
def tracker_status():
    status = open(os.path.join(main_path,'tracker','status.txt'),"r")
    content = status.read()
    if content == ("on") or content == (""):
        print("Tracker is ON")
    elif content == ("off"):
        print("Tracker is OFF")

# Count days working on it ✨
def count_on():
    status = open(os.path.join(main_path,'tracker','status.txt'),"r")
    content = status.read()

    today = date.today()
    yesterdayy = today - timedelta(days = 1)
    yesterday = str(yesterdayy)

    check_file = os.path.exists(os.path.join(main_path,'autogenarated_files',yesterday+'.txt'))
    if content == ('off'):
        checkfileoff = os.path.exists(os.path.join(main_path,'autogenarated_files',yesterday+'.txt'))
        if checkfileoff == (True):
            os.system("del /f "+os.path.join(main_path,'autogenarated_files',yesterday+'.txt'))
            StopIteration()  
        else:
            StopIteration()        
    elif check_file == (True):
        read_track_on = open(os.path.join(main_path,'tracker','track_on.txt'),'r')
        reading_track_on = read_track_on.read()
        words = reading_track_on.split()
        if len(words) == (0):
            StopIteration()
            print('ALERT: NO TRACKER!')
            print()
            os.system("del /f "+os.path.join(main_path,'autogenarated_files',yesterday+'.txt'))
        else:
            replace_dirt_tracker_on = reading_track_on.replace('.txt','')
            track_on_what_check = os.path.exists(os.path.join(main_path,'tracker',reading_track_on))
            if track_on_what_check == (False):
                open(os.path.join(main_path,'tracker',reading_track_on),'a').close
                write_new_tracked = open(os.path.join(main_path,'tracker',reading_track_on),'w')
                write_new_tracked.write('1')
                print('Working on '+replace_dirt_tracker_on+' '+ 'since, '+'1'+' day.')
                print()
                os.system("del /f "+os.path.join(main_path,'autogenarated_files',yesterday+'.txt'))
            else:
                read_tracked_file = open(os.path.join(main_path,'tracker',reading_track_on),'r')
                read_tracked_file_read = read_tracked_file.read()
                split_tracked = read_tracked_file_read.split()
                if len(split_tracked) == (0):
                    write_tracked_file = open(os.path.join(main_path,'tracker',reading_track_on),'w')
                    write_tracked_file.write('1')
                    print('Working on '+replace_dirt_tracker_on+' '+ 'since, '+'1'+' day.')
                    print()
                    os.system("del /f "+os.path.join(main_path,'autogenarated_files',yesterday+'.txt'))
                else:
                    int_read_tracked = int(read_tracked_file_read)
                    plus_one_tracked = int_read_tracked+1
                    write_tracked_file = open(os.path.join(main_path,'tracker',reading_track_on),'w')
                    hey_iam_done = str(plus_one_tracked)
                    write_tracked_file.write(hey_iam_done)
                    print('Working on '+replace_dirt_tracker_on+' '+ 'since, '+hey_iam_done+' days.')
                    print()
                    os.system("del /f "+os.path.join(main_path,'autogenarated_files',yesterday+'.txt'))

# Set tracker on or off
def status_writer(self):
    status = open(os.path.join(main_path,'tracker','status.txt'),"w")
    status.write(self)
    count_on()


# Main tracker
def tracker():
    # Take this input from user
    dir = (r"C:\Users\athar\OneDrive\Documents\projects")
    filename = os.listdir(dir)
    for filenames in filename:
        print(filenames)
    completer = MyCompleter(filename)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    track_on_file = input('ADD FILE TO TRACK: ')
    if track_on_file == (""):
        StopIteration()
    else:
        # Update track_on file
        istrackfile = (os.path.exists(os.path.join(dir,track_on_file)))
        if istrackfile == (False):
            print("FALSE DIR")
            StopIteration()
        else:
            track_file = open(os.path.join(main_path,'tracker','track_on.txt'),'w')
            track_file.write(track_on_file+'.txt')
    completer_on()