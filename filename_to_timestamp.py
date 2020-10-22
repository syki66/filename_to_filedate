from datetime import datetime
import os

extension_list = [".jpg", ".jpeg", ".png", ".gif"]

duplicate_count = 2

def convertFilename(filename):
    timestamp = os.path.getmtime(filename)
    date = datetime.fromtimestamp(timestamp)
        
    new_name = f'{date.year:04}-{date.month:02}-{date.day:02}_{date.hour:02}-{date.minute:02}-{date.second:02}'
    extension = filename[filename.rfind('.'):].lower()

    if extension in extension_list:
        global duplicate_count
        try:
            os.rename(filename, new_name+extension)
            duplicate_count = 2
            print(f'CHANGED: {filename}')

        except FileExistsError:
            

            os.rename(filename, f'{new_name}_{duplicate_count}{extension}')
            duplicate_count += 1

            print(f'CHANGED, BUT I INCREASED 1 SECOND BECAUSE FILE NAME ALREADY EXIST: {filename}')




        '''
        if isFilenameDuplicate(previous_name, new_name):
            os.rename(filename, new_name+extension)
            os.rename()
            print(f'CHANGED, BUT I INCREASED 1 SECOND BECAUSE FILE NAME ALREADY EXIST: {filename}')
        else:
            os.rename(filename, new_name+extension)
            print(f'CHANGED: {filename}')
        '''



user_input = input("If you type \"YES\" or \"Y\", The image files are renamed to timestamp\n")
yes = True if (user_input.lower() == 'y' or user_input.lower() == 'yes') else False

if (yes):
    print("CHANGING IMAGE FILES NAME...")
    for f in os.listdir():
        convertFilename(f)
            
else:
    print("GOOD BYE")

input("\nPRESS ENTER TO EXIT.")