import PIL
from PIL import Image
from PIL.ExifTags import TAGS
import os




for i in os.listdir():

    # path to the image or video
    imagename = i


    try:
        # read the image data using PIL
        image = Image.open(imagename)



        # extract EXIF data
        exifdata = image.getexif()

        print(i)
        if 36867 in exifdata:
            print(f'DateTimeOriginal : {exifdata[36867]}')
        if 36868 in exifdata:
            print(f'DateTimeDigitized : {exifdata[36868]}')
        if 306 in exifdata:
            print(f'DateTime : {exifdata[306]}')
        print("---------------------------\n")


    except Exception as e:

        print(f'errorName:{e}')



# # path to the image or video
# imagename = "IMG_2616.JPG"

# # read the image data using PIL
# image = Image.open(imagename)



# exifdata = image.getexif()

# if 36867 in exifdata:
#     print(f'DateTimeOriginal : {exifdata[36867]}')
# if 36868 in exifdata:
#     print(f'DateTimeDigitized : {exifdata[36868]}')
# if 306 in exifdata:
#     print(f'DateTime : {exifdata[306]}')




'''
DateTime
DateTimeOriginal
DateTimeDigitized
수정한날짜
만든날짜

이렇게 비교해서 가장 오래된 timestamp로 결정하기
'''
