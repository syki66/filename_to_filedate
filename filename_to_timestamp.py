from datetime import datetime
import os

extension_list = [".jpg", ".jpeg", ".png", ".gif"]

for f in os.listdir():
    timestamp = os.path.getmtime(f)
    date = datetime.fromtimestamp(timestamp)
    
    new_name = f'{date.year:04}-{date.month:02}-{date.day:02}_{date.hour:02}-{date.minute:02}-{date.second:02}'
    extension = f[f.rfind('.'):].lower()

    if extension in extension_list:
        os.rename(f, new_name+extension)
        print(f'changed: {f}')
    else:
        pass
