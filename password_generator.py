import random
import array, json
import pyperclip, os

main_path = os.path.dirname(__file__)

def password():
    MAX_LEN = 14

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']
    
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
    
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
            '*', '(', ')', '<']
    

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    
    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but 
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    
    
    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined 
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
    
        # convert temporary password into array and shuffle to 
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    
    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
            password = password + x
            
    # COPY PASSWORD TO CLIPBOARD & WRITE IT:)
    input1 = input("ENTER MEDIA-HANDLE: ")
    if input1 == (""):
        StopIteration()
    else:
        input2 = input("ENTER USERNAME: ")
        if input2 == (""):
            StopIteration()
        else:
            try: 
                with open ((os.path.join(main_path,"paths.json")),"r") as f:
                    data1 = json.load(f)
                    dir01 = data1["PAINT_TXT"]
            except:
                print("FIRST-TIME WRITING PASSWORD-PATH")
                with open ((os.path.join(main_path,"paths.json")),"r") as f:
                    data = json.load(f)
                change = {"PAINT_TXT":None}
                data.update(change)
                with open((os.path.join(main_path,"paths.json")),"a") as f:
                    g = open((os.path.join(main_path,"paths.json")),"r+")
                    g.truncate(0)
                    json.dump(data,f,indent=4)
            with open ((os.path.join(main_path,"paths.json")),"r") as f:
                    data1 = json.load(f)
                    dir01 = data1["PAINT_TXT"]
            if dir01 == (None):
                while True:
                    inp = input("PASTE YOUR SECRET FOLDER PATH (NOT ADMIN PATH): ")
                    check_dir = os.path.exists(inp)
                    if check_dir == (True):
                        change = {"PAINT_TXT":(os.path.join(inp,("paint.txt")))}
                        data1.update(change)
                        with open((os.path.join(main_path,"paths.json")),"a") as f:
                            g = open((os.path.join(main_path,"paths.json")),"r+")
                            g.truncate(0)
                            json.dump(data1,f,indent=4)
                            print()
                            print("This function is made for management of PASSWORDS :)")
                            print("Enter a "+'"'+"?"+'" '+"mark to know particular documentation of this function.")
                            print()
                            break
                    else:
                        print("DIR DOES'NT EXISTS :)")
        with open ((os.path.join(main_path,"paths.json")),"r") as f:
            data = json.load(f)
            dir = data["PAINT_TXT"]
        pyperclip.copy(password)
        file_path = (dir)
        with open(file_path, "a+") as np_file:
            np_file.write(input1+"\n"+input2+"  -  "+password+ "\n")

