import commands
import features
import tracking_master  
import readline
import processor
import os
readline.set_completer(commands.completer.complete)
readline.parse_and_bind('tab: complete')
# All ESSENTIAL DIRS and FILES CHECKER
features.check_dir()
# MAXIMISES PROGRAM 
features.maximize()
# FUNCTIONALITY FOR blank inputs
features.clear_command_history()
# Count greeting (For only one time a day)
features.greet()
# FUNCTIONALITY FOR tracking master
tracking_master.count_on()

main_path = os.path.dirname(__file__)

while True:
    x = list(input("TYPE IN HERE: ").lower().strip().split())
    processor.processor(x)
    features.check_empty_command()

