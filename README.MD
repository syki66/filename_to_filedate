# FilenameToFiledate

파일의 이름을 파일의 `날짜`로 변경해주는 프로그램

---

## Feature

- 파일의 이름을 파일의 날짜로 변경함
    - 2020년 1월 1일 오후 8시 22분 33초 => `2020_01_01-20_22_33.EXT`
- 프로그램을 작동시킨 디렉토리에 있는 파일들만 이름이 변경됨
- `원본 이름` -> `해시값` -> `수정된 이름` 순으로 변경됨
- 미리 지정한 확장자만 파일 이름이 변경됨
    - 현재 변경되는 확장자 : `.JPG`, `.JPEG`, `.PNG`, `.GIF`, `.HEIC`, `.HEIF`, `.TIF`, `.TIFF`, `.MP4`, `.MOV`, `.AVI`, `.WMV`, `.MPG`, `.MPEG`
- 아래 목록중 가장 오래된 날짜를 기준으로함
    - 사진 : `DateTime`, `DateTimeOriginal`, `DateTimeDigitized`, `Date created`, `Date modified`
    - 비디오 : `Date created`, `Date modified`, `encoded_date`, `tagged_date`
- 중복 네이밍이 발생할 경우, 초단위를 1초씩 올려서 중복 해결
    - `2020_02_02-22_22_01.EXT` => `2020_02_02-22_22_01.EXT`
    - `2020_02_02-22_22_01.EXT` => `2020_02_02-22_22_02.EXT`
    - `2020_02_02-22_22_02.EXT` => `2020_02_02-22_22_03.EXT`
    - `2020_02_02-22_22_02.EXT` => `2020_02_02-22_22_04.EXT`
    - `2020_02_02-22_22_04.EXT` => `2020_02_02-22_22_05.EXT`

---

## Caution

- 프로그램 실행 시 오류가 뜨게 된다면, `바이러스 및 위협 방지`에 들어가서 이 프로그램을 `디바이스에서 허용` 해주어야함
- 프로그램 실행 후 이미 `바뀐 파일 이름은 되돌릴 수 없음`
- 확장자가 소문자일 경우 `대문자`로 변경됨

---

## Extra Tools

- [hour_converter.py](https://github.com/syki66/filename_to_filedate/blob/master/extra_tools/hour_converter.py) : 시간대를 변경해주는 툴
- [second_converter.py](https://github.com/syki66/filename_to_filedate/blob/master/extra_tools/second_converter.py) : 초단위를 변경해주는 툴
- [line_up_seconds.py](https://github.com/syki66/filename_to_filedate/blob/master/extra_tools/line_up_seconds.py) : 기준값 날짜로 줄세워주는 툴
- [timestamp_to_date_converter.py](https://github.com/syki66/filename_to_filedate/blob/master/extra_tools/timestamp_to_date_converter.py) : 타임스탬프를 날짜로 변환해주는 툴

---

## Change Log

- [CHANGELOG.MD](https://github.com/syki66/filename_to_timestamp/blob/master/CHANGELOG.MD)

---

## Todo List

- `heic`, `heif`의 exif를 자체적으로 해결하기
- gui 환경 구성하면서 보조툴 기능 병합
- 코드 분리하기
- 원본 파일이름 남길지 선택 옵션
- YYYY MM DD 이런것들 사이에 넣을수 있는 문자를 커스터마이징 할수 있게하기

---

## Build

> pyinstaller 사용시, 같은 디렉토리에 `filename_to_datetime.py`, `exiftool.exe`, `pen.ico` 위치시키고, 및 `pymediainfo`에 있는 dll 파일 위치 넣어주기

```
pyinstaller --onefile --icon pen.ico --add-data "exiftool.exe;." --add-binary "C:/Users/syki66/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/pymediainfo/MediaInfo.dll;." filename_to_datetime.py
```