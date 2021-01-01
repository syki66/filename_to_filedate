import os
import re

print('주의 : 같은 디렉토리에 있는 모든 파일이 변환 과정을 거침\n')
print('\"YYYY-MM-DD_hh-mm-ss.ext\" 이 형식의 이름을 가진 파일만 변환됨')
print('입력은 \"YYYY-MM-DD_hh-mm-ss\" 형식으로 입력해야됨')
print('입력 날짜 기준으로 초단위 오름차순으로 파일의 이름을 변경함')
print('초단위가 99를 초과할때 분단위가 1 올라감\n')

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

def changeName(date):
    new_date = date.rsplit('-', 2)[0]
    minute = int(date.rsplit('-', 2)[1])
    second = int(date.rsplit('-', 2)[2])

    for file in os.listdir():
        try:
            old_filename = file
            old_name = old_filename.split(".")[0]
            ext = old_filename.split(".")[1]
            if isValidValue(old_name, '\d\d\d\d-\d\d-\d\d_\d\d-\d\d-\d\d', 19):
                new_filename = f'{new_date}-{minute:02}-{second:02}.{ext}'
                os.rename(old_filename, new_filename)
                print(f'변경됨 : {old_filename} -> {new_filename}')
                if (second >= 99):
                    minute += 1
                    second = 0
                else:
                    second += 1
        except Exception as e:
            print(f'에러발생 : \"{file}\" 파일의 {e} \"YYYY-MM-DD_hh-mm-ss.ext\"')

try:
    date = input("시간 값을 입력해주세요 : ")
    if (isValidValue(date, '\d\d\d\d-\d\d-\d\d_\d\d-\d\d-\d\d', 19)):
        changeName(date)
except Exception as e:
    print(f'\n에러발생 : 입력값의 {e} \"YYYY-MM-DD_hh-mm-ss\"')

input("\n엔터를 누르면 종료됨")
