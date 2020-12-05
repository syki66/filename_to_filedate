import os
import re

print('주의 : 같은 디렉토리에 있는 모든 파일이 변환 과정을 거침\n')
print('특정 날짜를 입력하면 초단위를 1초 차이로 순서대로 변경해줌')
print('입력은 \"2020-01-01_09-30\" 이런식으로 초 단위는 비워둔 채로 입력')
print('\"2020-01-01_11-11-23.ext\" 이 형식의 파일만 변환됨\n')

def isValidValue(value, regex, maxLength):
    if len(value) > maxLength:
        raise Exception('형식이 맞지 않습니다.')
    else:
        p = re.compile(regex)
        m = p.match(value)
        if m is not None:
            return True
        else:
            raise Exception('형식이 맞지 않습니다.')

def changeName(new_date):
    for file in enumerate(os.listdir()):
        try:
            index = file[0]
            old_filename = file[1]
            old_name = file[1].split(".")[0]
            ext = file[1].split(".")[1]
            if isValidValue(old_name, '\d\d\d\d-\d\d-\d\d_\d\d-\d\d-\d\d', 19):        
                new_filename = f'{new_date}-{index:02}.{ext}'
                os.rename(old_filename, new_filename)
                print(f'변경됨 : {old_filename} -> {new_filename}')
        except Exception as e:
            print(f'에러발생 : \"{file[1]}\" 파일의 {e} \"YYYY-MM-DD_hh-mm-ss.ext\"')

try:
    date = input("시간 값을 입력해주세요 : ")
    if (isValidValue(date, '\d\d\d\d-\d\d-\d\d_\d\d-\d\d', 16)):
        changeName(date)
except Exception as e:
    print(f'\n에러발생 : {e} \"YYYY-MM-DD_hh-mm\"')

input("\n엔터를 누르면 종료됨")
