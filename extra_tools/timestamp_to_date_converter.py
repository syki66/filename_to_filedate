import os
from datetime import datetime

print('주의 : 같은 디렉토리에 있는 모든 파일이 변환 과정을 거침\n')
print('확장자는 대문자로 변경됨')
print('타임스탬프를 날짜값으로 변경함')
print('\"\d\d\d\d\d\d\d\d\d\d.ext\" 형식의 파일만 변환됨\n')

input('\"ENTER\" 키를 누르면 변환 실행\n')

for filename in os.listdir():
    try:
        ts = int(filename.split('.')[0])
        ext = filename.split('.')[1].upper()
        
        date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
        new_name = f'{date}.{ext}'

        os.rename(filename, new_name)
        print(f'변경됨: {filename} -> {new_name}')
        
    except Exception as e:
        print(f'에러발생: {e}')