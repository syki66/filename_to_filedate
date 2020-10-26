from datetime import datetime
import os

# 사전형으로 해야됨. 그러고 오름차순

extensions = [".JPG", ".JPEG", ".PNG", ".GIF", ".HEIC", "HEIF"]


def getFileDate(filename):
    timestamp = os.path.getmtime(filename)
    date = datetime.fromtimestamp(timestamp)
    
    new_name = f'{date.year:04}-{date.month:02}-{date.day:02}_{date.hour:02}-{date.minute:02}-{date.second:02}'
    return new_name



dic = {}
for ext in extensions:
    temp = {}
    for filename in os.listdir():
        if (filename[filename.rfind('.'):].upper() == ext):
            temp[filename] = getFileDate(filename)
    dic[ext] = temp




print(dic)


'''
# classified_files = []

def getFileDate(filename):
    timestamp = os.path.getmtime(filename)
    date = datetime.fromtimestamp(timestamp)
    
    new_name = f'{date.year:04}-{date.month:02}-{date.day:02}_{date.hour:02}-{date.minute:02}-{date.second:02}'
    return new_name



for extension in extensions:
    temp = []
    for filename in os.listdir():
        if (filename[filename.rfind('.'):].upper() == extension):
            temp.append(filename)
    classified_files.append(temp)

print(classified_files)


modified_dates = []

for i, files in enumerate(classified_files):
    temp = []
    for f in files:
        temp.append(f'{getFileDate(f)}{extensions[i]}')
    modified_dates.append(temp)

for i in modified_dates:
    for f in i:
        print(f)

'''


'''
duplicate_count = 2
converted_file_count = 0

def convertFileName(filename, extension):
    timestamp = os.path.getmtime(filename)
    date = datetime.fromtimestamp(timestamp)
        
    new_name = f'{date.year:04}-{date.month:02}-{date.day:02}_{date.hour:02}-{date.minute:02}-{date.second:02}'

    try:
        os.rename(filename, f'{new_name}{extension}')
        duplicate_count = 2
        print(f'CHANGED: {filename}')

    except FileExistsError:
        os.rename(filename, f'{new_name}_{duplicate_count}{extension}')
        duplicate_count += 1

        print(f'CHANGED, BUT I INCREASED 1 SECOND BECAUSE FILE NAME ALREADY EXIST: {filename}')

    #global converted_file_count
    #converted_file_count += 1

def wipeUpFileName(ext_list):
    import random
    prefix = random.randint(1,100000)

    name_count = 0
    for extension in ext_list:
        for filename in os.listdir():
            
            if (filename[filename.rfind('.'):].upper() == extension):
                os.rename(filename, f'{prefix}_{name_count}{extension}')
                name_count+=1


user_input = input("If you type \"YES\" or \"Y\", The image files are renamed to timestamp\n")
yes = True if (user_input.lower() == 'y' or user_input.lower() == 'yes') else False

if (yes):
    print("\nCHANGING IMAGE FILES NAME...\n")

    # wipeUpFileName(extension_list)

    for f in os.listdir():
        convertFileName(f, extension_list)
    
    print(f'\nFINISHED. CONVERTED {converted_file_count} FILES')
else:
    print("GOOD BYE")

input("\nPRESS ENTER TO EXIT.")

'''