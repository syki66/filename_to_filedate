import subprocess

input_file = "test.HEIC"
exe = "exiftool"
process = subprocess.Popen([exe, input_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

info = {}
for output in process.stdout:
    
    line = output.strip().split(":",1)
    info[line[0].strip()] = line[1].strip()
    print(line)

print(info['Date/Time Original'])
print(info['Create Date'])
print(info['Modify Date'])