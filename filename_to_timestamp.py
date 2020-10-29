from datetime import datetime
import os
from collections import OrderedDict

extensions = [".JPG", ".JPEG", ".PNG", ".GIF", ".HEIC", "HEIF"]

# 파일의 날짜 얻기, (찍은 날짜 존재하면 찍은 날짜로 대입하는 것으로 변경해야됨)
def getFileDate(filename):
    timestamp = os.path.getmtime(filename)
    date = datetime.fromtimestamp(timestamp)
    
    new_name = f'{date.year:04}-{date.month:02}-{date.day:02}_{date.hour:02}-{date.minute:02}-{date.second:02}'
    return new_name

# 찍은 날짜가 존재하는지 함수 추가하기
# heic 파일은 jpg 변환후 찍은날짜 가져와야됨

# 각 확장자마다, 날짜기준 오름차순으로 만든 OrderedDict형을 반환함
def sortFiles(ext_list):
    files = {}
    for ext in ext_list:
        temp = {}
        for filename in os.listdir():
            if (filename[filename.rfind('.'):].upper() == ext):
                temp[filename] = f'{getFileDate(filename)}{ext}'
        files[ext] = OrderedDict(sorted(temp.items(),key=lambda x: x[1]))
    return files

# 파일명 재조립하기
def reassemble(value, number):
    date = value[ :value.rfind('-')]
    second = int(value[value.rfind('-')+1 : value.rfind('.')])
    extension = value[value.rfind('.') : ]
    return f'{date}-{second+number:02}{extension}'

# 날짜가 중복된 파일에만 중복이 아닐때까지 초단위 시간 올리기
def handleDuplicates(dict):
    for ext in extensions:
        prev_values = []
        for key, value in dict[ext].items():
            dict_without_me = { k:v for k, v in dict[ext].items() if ( k != key) }
            num = 0
            # 중복파일이 존재하고 이전에 존재했던 값이 아닐때까지 1씩 계속 증가시키기
            while (reassemble(value, num) in dict_without_me.values() and reassemble(value, num) in prev_values ):
                num += 1
            dict[ext][key] = reassemble(value, num)
            prev_values.append(reassemble(value, num))
    return dict

# 파일이름 변경 추적 현황을 콘솔에 출력해주기
original_dict = sortFiles(extensions)
def printFilenameStatus(extension, key, value):
    if (original_dict[extension][key] != value):
        print(f'CHANGED: "{key}" -> "{original_dict[extension][key]}" -> "{value}"')
    else:
        print(f'CHANGED: "{key}" -> "{value}"')

# 실제 파일이름 변경
converted_file_count = 0
def renameFiles(dict):
    global converted_file_count
    for ext in extensions:
        for key, value in dict[ext].items():
            os.rename(key, value)
            printFilenameStatus(ext, key, value)
            converted_file_count += 1

# 실행부
user_input = input("If you type \"YES\" or \"Y\", The image files are renamed to timestamp\n")
yes = True if (user_input.lower() == 'y' or user_input.lower() == 'yes') else False

if (yes):
    print("\nCHANGING IMAGE FILES NAME...\n")

    refined_dict = handleDuplicates(sortFiles(extensions))    
    renameFiles(refined_dict)

    print(f'\nFINISHED. CONVERTED {converted_file_count} FILES')
else:
    print("GOOD BYE")

input("\nPRESS ENTER TO EXIT.")

# 한번 이름 싹 밀어주는 함수 추가해야됨 (그래도 예외처리도 넣어주기)


'''
def wipeUpFileName(ext_list):
    import random
    prefix = random.randint(1,100000)

    name_count = 0
    for extension in ext_list:
        for filename in os.listdir():
            
            if (filename[filename.rfind('.'):].upper() == extension):
                os.rename(filename, f'{prefix}_{name_count}{extension}')
                name_count+=1
'''