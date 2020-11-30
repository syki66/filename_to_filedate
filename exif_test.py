from PIL import Image
import os
from datetime import datetime

#exif 변환해야됨

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
    image = Image.open(filename)
    exif = image.getexif()

    dateArray = []
    if 36867 in exif:
        dateTimeOriginal = f'{int(exif[36867][0:4]):04}-{int(exif[36867][5:7]):02}-{int(exif[36867][8:10]):02}_{int(exif[36867][11:13]):02}-{int(exif[36867][14:16]):02}-{int(exif[36867][17:19]):02}'
        dateArray.append(dateTimeOriginal)
    if 36868 in exif:
        dateTimeDigitized = f'{int(exif[36868][0:4]):04}-{int(exif[36868][5:7]):02}-{int(exif[36868][8:10]):02}_{int(exif[36868][11:13]):02}-{int(exif[36868][14:16]):02}-{int(exif[36868][17:19]):02}'
        dateArray.append(dateTimeDigitized)
    if 306 in exif:
        dateTime = f'{int(exif[306][0:4]):04}-{int(exif[306][5:7]):02}-{int(exif[306][8:10]):02}_{int(exif[306][11:13]):02}-{int(exif[306][14:16]):02}-{int(exif[306][17:19]):02}'
        dateArray.append(dateTime)
    return dateArray

def pickOldestDate(filename):
    return getFileDate(filename) + getExifDate(filename)



for file in os.listdir():


    try:
        print(file)
        print(pickOldestDate(file))
        print("")

    except Exception as e:

        print(f'errorName:{e}')



# imagename = "IMG_2620.JPG"
# print(pickOldestDate(imagename))






'''
DateTime
DateTimeOriginal
DateTimeDigitized
Date created
Date modified
'''
