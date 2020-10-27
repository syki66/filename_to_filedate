from datetime import datetime
import os
from collections import Counter
from collections import OrderedDict

extensions = [".JPG", ".JPEG", ".PNG", ".GIF", ".HEIC", "HEIF", ".TXT"]

# 파일의 날짜 얻기, (찍은 날짜 존재하면 찍은 날짜로 대입하는 것으로 변경해야됨)
def getFileDate(filename):
    timestamp = os.path.getmtime(filename)
    date = datetime.fromtimestamp(timestamp)
    
    new_name = f'{date.year:04}-{date.month:02}-{date.day:02}_{date.hour:02}-{date.minute:02}-{date.second:02}'
    return new_name

# 찍은 날짜가 존재하는지 함수 추가하기

# 각 확장자마다, 날짜기준 오름차순으로 만든 OrderedDict형을 반환함
def sortFiles(ext_list):
    files = {}
    for ext in ext_list:
        temp = {}
        for filename in os.listdir():
            if (filename[filename.rfind('.'):].upper() == ext):
                temp[filename] = getFileDate(filename)
        files[ext] = OrderedDict(sorted(temp.items(),key=lambda x: x[1]))
    return files

# 파일명 재조립하기
def reassemble(value, number):
    date = value[ :value.rfind('-')]
    second = int(value[value.rfind('-')+1: ])
    return f'{date}-{second+number:02}'

# 날짜가 중복된 파일에만 중복이 아닐때까지 초단위 시간 올리기
def renameDuplicateFiles(dict):
    for ext in extensions:
        prev_values = []
        for key, value in dict[ext].items():
            dict_without_me = { k:v for k, v in dict[ext].items() if ( k != key) }
            num = 0
            while (reassemble(value, num) in dict_without_me.values() and reassemble(value, num) in prev_values ):
                num += 1           
            dict[ext][key] = reassemble(value, num)
            prev_values.append(reassemble(value, num))
    return dict



'''
def renameFiles:
    print ( renameDuplicateFiles(sortFiles(extensions)) )
'''







def testDuplicateFunc():
    original = []
    modified = []

    for ext in extensions:
        for i in sortFiles(extensions)[ext].items():
            original.append(i)

    for ext in extensions:
        for i in renameDuplicateFiles(sortFiles(extensions))[ext].items():
            modified.append(i)

    print(len(original), len(modified))

    for i in range(len(original)):
        print(f'변경전: {original[i]},  변경후: {modified[i]}')

testDuplicateFunc()

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