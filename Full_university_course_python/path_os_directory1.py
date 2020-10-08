import os
from os.path import join
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            thefile = os.path.join(dirname, filename)
            size = os.path.getsize(thefile)
            if size == 2578 or size == 2565:
                print('T-Mobile:', thefile)
                os.remove(thefile)
                continue
            fhand = open(thefile, 'r')
            lines = list()
            for line in fhand:
                lines.append(line)
            fhand.close()
            if len(lines) == 3 and lines[2].startswith('Sent from my iPhone'):
                print('iPhone:', thefile)
                os.remove(thefile)
                continue


"""
# Don't overwrite the file
if os.path.exists(fname):
    if input('Replace ' + fname + ' (Y/n)?') != 'Y':
        print('Data not copied')
        exit()
    print('Replacing', fname)

fhand = open(fname, 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied to', fname)
fhand.close()
"""