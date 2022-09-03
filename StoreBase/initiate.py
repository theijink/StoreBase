from parameters import *
import os
import csv

path, dirs, files = next(os.walk('.'))

## fix directories
if not bindirectory in dirs:
    os.mkdir(bindirectory)
else:
    pass
if not stickersdirectory in dirs:
    os.mkdir(stickersdirectory)
else:
    pass

## fix bin directory files
p,d,f = next(os.walk(bindirectory))
if not activityfilename.split('/')[-1] in f:
    file=open(activityfilename, 'w')
    writer=csv.DictWriter(file, fieldnames=activityfileheader, delimiter=',')
    writer.writeheader()
    file.close()
else:
    pass
if not credentialsfilename.split('/')[-1] in f:
    file=open(credentialsfilename, 'w')
    writer=csv.DictWriter(file, fieldnames=credentialsfileheader, delimiter=',')
    writer.writeheader()
    file.close()
else:
    pass
if not databasefilename.split('/')[-1] in f:
    file=open(databasefilename, 'w')
    writer=csv.DictWriter(file, fieldnames=databasefileheader, delimiter=',')
    writer.writeheader()
    file.close()    
else:
    pass

p,d,f = next(os.walk(stickersdirectory))
## fix stickes directory files
if not stickerfilename.split('/')[-1] in f:
    file=open(stickerfilename, 'w')
    writer=csv.DictWriter(file, fieldnames=stickerfileheader, delimiter=',')
    writer.writeheader()
    file.close()    
else:
    pass
