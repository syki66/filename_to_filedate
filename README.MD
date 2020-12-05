# filename_to_filedate

미디어 파일의 이름을 파일의 `날짜`로 변경해주는 프로그램

---

# Feature

- 파일의 이름을 파일의 날짜로 변경함
    - 2020년 1월 1일 오후 8시 22분 33초 => `2020_01_01-20_22_33`
- 아래 목록중 가장 오래된 날짜를 기준으로함
    - 사진 : `DateTime`, `DateTimeOriginal`, `DateTimeDigitized`, `Date created`, `Date modified`
    - 비디오 : `Date created`, `Date modified`, `encoded_date`, `tagged_date`
- 미리 지정한 확정자만 파일 이름이 변경됨
    - 현재 변경되는 확장자 : `.JPG`, `.JPEG`, `.PNG`, `.GIF`, `.HEIC`, `.HEIF`, `.TIF`, `.TIFF`, `.MP4`, `.AVI`, `.MOV`, `.K3G`, `.JPS`
- 중복 네이밍이 발생할 경우, 초단위를 1초씩 올려서 중복 해결 *(뒤에 파일 날짜를 침범할 경우 뒤에 있는 파일도 같이 초단위를 밀어버림)*
    - 예를 들어 `2020_01_01-11_11_11` 파일 2개, `2020_01_01-11_11_12` 파일이 1개 존재할 경우
    - 먼저 전자의 두개 파일은 `2020_01_01-11_11_11`, `2020_01_01-11_11_12`으로 변경 (이름 순서는 원본 파일이름의 오름차순)
    - 후자의 1개 파일은 `2020_01_01-11_11_13`으로 변경
- 이 프로그램을 실행하면 같은 디렉토리에 있는 파일들만 이름이 변경됨

---

# Caution

- 프로그램 실행 시 오류가 뜨게 된다면, `바이러스 및 위협 방지`에 들어가서 이 프로그램을 `디바이스에서 허용` 해주어야함
- 프로그램 실행 후 이미 바뀐 파일 이름은 되돌릴 수 없음
- 확장자가 소문자일 경우 대문자로 변경됨
- `원본 이름` -> `해시값` -> `수정된 이름` 순으로 변경되어 중복이름으로 인한 에러는 사실상 발생하기 어려우나, 만에 하나 해시값이 중복될 경우, 재실행 하면 해결됨
- 오래된 비디오 파일 *(UTC +00:00)* 이나 해외에서 찍은 일부 미디어 파일 *(해당지역시간)* 의 경우, 현재지역시간과의 차이 만큼 시간 오차가 날 수도 있음
    - [hour_converter.py](https://github.com/syki66/filename_to_filedate/blob/master/extra_tools/hour_converter.py)를 사용하여 시간대를 수동으로 변경할 수 있음

---

# 변경 로그

- [CHANGELOG.MD](https://github.com/syki66/filename_to_timestamp/blob/master/CHANGELOG.MD)

---

# Todo List

- `heic`, `heif`의 exif를 자체적으로 해결하기
<!-- - 카카오톡 다운로드 파일은 제목에서 날짜 추출 하기 -->
- gui 환경 구성하면서 보조툴 기능 병합
- 코드 분리하기

---

# pyinstaller 사용시

> 같은 디렉토리에 `filename_to_datetime.py`, `exiftool.exe`, `pen.ico` 위치시키고, 및 `pymediainfo`에 있는 dll 파일 위치 넣어주기

```
pyinstaller --onefile --icon pen.ico --add-data "exiftool.exe;." --add-binary "C:/Users/syki66/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/pymediainfo/MediaInfo.dll;." filename_to_datetime.py
```