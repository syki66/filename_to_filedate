from datetime import datetime, timedelta
import os

print('주의 : 같은 디렉토리에 있는 모든 파일이 변환 과정을 거침\n')
print('\"+\"숫자 또는 \"-숫자\"를 이용해서 시간값만 변경가능')
print('9시간 이전으로 이름변경을 한다면 \"-9\"를 입력')
print('\"2020-01-01_11-11-23.ext\" 이 형식일 경우만 변환됨\n')

def changeHour(hour):
    for old_filename in os.listdir():
        try:
            file_date = old_filename.split(".")[0]
            ext = f'{old_filename.split(".")[1]}'

            old_date = datetime.strptime(file_date, "%Y-%m-%d_%H-%M-%S")
            new_date= old_date + timedelta(hours=hour)
            new_filename = f'{new_date.year:04}-{new_date.month:02}-{new_date.day:02}_{new_date.hour:02}-{new_date.minute:02}-{new_date.second:02}.{ext}'

            os.rename(old_filename, new_filename)
            print(f'변경됨 : {old_filename} -> {new_filename}')
        except Exception as e:
            print(f'에러발생 : \"{old_filename}\" {e}')

try:
    hour = int(input("시간 값을 입력해주세요 : "))
    changeHour(hour)
except Exception as e:
    print(f'에러발생 : {e}')

input("\n엔터를 누르면 종료됨")