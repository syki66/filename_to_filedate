from pymediainfo import MediaInfo
from datetime import datetime
from dateutil import tz

media_info = MediaInfo.parse("test.mp4")

timestring = media_info.tracks[2].to_data()['encoded_date'].split('UTC ')[1]
print(media_info.tracks[2].to_data()['encoded_date'].split('UTC ')[1])


from_zone = tz.tzutc()
to_zone = tz.tzlocal()

utc = datetime.strptime(timestring, '%Y-%m-%d %H:%M:%S')
utc = utc.replace(tzinfo=from_zone)

central = utc.astimezone(to_zone)

print(central)