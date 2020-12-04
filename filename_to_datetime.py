from datetime import datetime
import os
from collections import OrderedDict
import hashlib
from PIL import Image
from pymediainfo import MediaInfo
from dateutil import tz

extensions = [".JPG", ".JPEG", ".PNG", ".GIF", ".HEIC", ".HEIF", ".TIF", ".TIFF", ".MP4", ".AVI", ".MOV", ".K3G", ".JPS"]

print("PREPARING FOR RENAMING FILES...\n")

# get exif of HEIF HEIC image (heic 자체 지원 방법 찾으면 나중에 삭제할 예정)
def getHeicExif(filename):
    import subprocess
    dateArray = []
    def getDate(value):
        date = str(datetime.strptime(value, '%Y:%m:%d %H:%M:%S'))
        return f'{int(date[0:4]):04}-{int(date[5:7]):02}-{int(date[8:10]):02}_{int(date[11:13]):02}-{int(date[14:16]):02}-{int(date[17:19]):02}'
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    try:
        if filename.upper().endswith('.HEIC') or filename.upper().endswith('.HEIF'):
            exe = resource_path("exiftool.exe")
            process = subprocess.Popen([exe, filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            exif = {}
            for output in process.stdout:
                line = output.strip().split(":",1)
                exif[line[0].strip()] = line[1].strip()
            if 'Date/Time Original' in exif:
                dateArray.append(getDate(exif['Date/Time Original'].split('.')[0]))
            if 'Create Date' in exif:
                dateArray.append(getDate(exif['Create Date'].split('.')[0]))
            if 'Modify Date' in exif:
                dateArray.append(getDate(exif['Modify Date'].split('+')[0]))
    except:
        pass
    return dateArray

# get Dates of video metadata ("encoded_date", "tagged_date")
def getVideoDate(filename):
    dateArray = []
    def getDate(key):
        value = media_info.tracks[2].to_data()[key].split('UTC ')[1]
        utcDate = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        utcDate = utcDate.replace(tzinfo=tz.tzutc())
        localDate = str(utcDate.astimezone(tz.tzlocal())).split('+')[0]
        return f'{int(localDate[0:4]):04}-{int(localDate[5:7]):02}-{int(localDate[8:10]):02}_{int(localDate[11:13]):02}-{int(localDate[14:16]):02}-{int(localDate[17:19]):02}'
    try:
        media_info = MediaInfo.parse(filename)
        if 'encoded_date' in media_info.tracks[2].to_data():
            dateArray.append(getDate('encoded_date'))
        if 'tagged_date' in media_info.tracks[2].to_data():
            dateArray.append(getDate('tagged_date'))
    except:
        pass
    return dateArray

# get "Date created", "Date modified"
def getFileDate(filename):
    dateArray = []
    if os.path.getctime(filename) is not None:
        timestamp = os.path.getctime(filename)
        date = datetime.fromtimestamp(timestamp)
        dateCreated = f'{date.year:04}-{date.month:02}-{date.day:02}_{date.hour:02}-{date.minute:02}-{date.second:02}'
        dateArray.append(dateCreated)
    if os.path.getmtime(filename) is not None:
        timestamp = os.path.getmtime(filename)
        date = datetime.fromtimestamp(timestamp)
        dateModified = f'{date.year:04}-{date.month:02}-{date.day:02}_{date.hour:02}-{date.minute:02}-{date.second:02}'
        dateArray.append(dateModified)
    return dateArray

# get Dates of exif data ("DateTimeOriginal", "DateTimeDigitized", "DateTime")
def getExifDate(filename):
    dateArray = []
    Image.MAX_IMAGE_PIXELS = None # DecompressionBombWarning 안뜨게 하기
    try:
        image = Image.open(filename)
        exif = image.getexif()
        if 36867 in exif:
            dateTimeOriginal = f'{int(exif[36867][0:4]):04}-{int(exif[36867][5:7]):02}-{int(exif[36867][8:10]):02}_{int(exif[36867][11:13]):02}-{int(exif[36867][14:16]):02}-{int(exif[36867][17:19]):02}'
            dateArray.append(dateTimeOriginal)
        if 36868 in exif:
            dateTimeDigitized = f'{int(exif[36868][0:4]):04}-{int(exif[36868][5:7]):02}-{int(exif[36868][8:10]):02}_{int(exif[36868][11:13]):02}-{int(exif[36868][14:16]):02}-{int(exif[36868][17:19]):02}'
            dateArray.append(dateTimeDigitized)
        if 306 in exif:
            dateTime = f'{int(exif[306][0:4]):04}-{int(exif[306][5:7]):02}-{int(exif[306][8:10]):02}_{int(exif[306][11:13]):02}-{int(exif[306][14:16]):02}-{int(exif[306][17:19]):02}'
            dateArray.append(dateTime)
    # except Exception as e:
    #     print(e)
    except:
        pass
    return dateArray

# 가장 오래된 날짜만 반환해주는 함수
def pickOldestDate(filename):
    date = getFileDate(filename) + getExifDate(filename) + getVideoDate(filename) + getHeicExif(filename) # (heic, 삭제 예정)
    date.sort()
    return date[0]

# 각 확장자마다, 날짜기준 오름차순으로 만든 OrderedDict형을 반환함
def sortFiles():
    files = {}
    for ext in extensions:
        temp = {}
        for filename in os.listdir():
            if (filename[filename.rfind('.'):].upper() == ext):
                temp[filename] = f'{pickOldestDate(filename)}{ext}'
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
original_dict = sortFiles()
def printFilenameStatus(extension, key, value):
    if (original_dict[extension][key] != value):
        print(f'CHANGED: "{key}" -> "{original_dict[extension][key]}" -> "{value}"')
    else:
        print(f'CHANGED: "{key}" -> "{value}"')

# 파일 이름을 해시값으로 변환
def convertToHash(filename):
    encoded_name = filename.encode('utf-8')
    md5 = hashlib.new('md5')
    md5.update(encoded_name)
    hash_value = md5.hexdigest()
    return hash_value

# 파일 이름을 전부 해시값으로 변환 (중복 이름 에러 방지)
def wipeUpFileName(dict):
    for ext in extensions:
        for key, value in dict[ext].items():
            hashed_key = convertToHash(key)
            os.rename(key, hashed_key)

# 실제 파일이름 변경
converted_file_count = 0
def renameFiles(dict):
    global converted_file_count
    for ext in extensions:
        for key, value in dict[ext].items():
            hashed_key = convertToHash(key)
            os.rename(hashed_key, value)
            printFilenameStatus(ext, key, value)
            converted_file_count += 1

# 변환전 변환될 파일 개수 출력해주기
def ToBeConvertedCount(dict):
    count = 0
    for ext in extensions:
        count += len(dict[ext])
    return count

# 실행부
print('WARNING!! THIS OPERATION IS IRREVRERSIBLE!!\n')
print(f'YOUR CURRENT DIRECTORY IS \"{os.getcwd()}\"\n')
print(f'{ToBeConvertedCount(original_dict)} MEDIA FILES WILL BE RENAMED.\n')

user_input = input("IF YOU TYPE \"YES\" OR \"Y\", THE MEDIA FILES ARE RENAMED TO \"ORIGINAL FILE DATE\"\n>>> ")
yes = True if (user_input.lower() == 'y' or user_input.lower() == 'yes') else False

try:
    if (yes):
        print("\nCHANGING MEDIA FILES NAME...\n")

        refined_dict = handleDuplicates(sortFiles())
        wipeUpFileName(refined_dict)
        renameFiles(refined_dict)

        if converted_file_count == 0:
            print("NO FILES ARE RENAMED")
        else:
            print(f'\nFINISHED. {converted_file_count} FILES RENAMED')
    else:
        print("GOOD BYE")
except Exception as e:
    print("ERROR")
    print(e)

input("\nPRESS ENTER TO EXIT.")
