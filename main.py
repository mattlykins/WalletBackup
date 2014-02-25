import glob
import os
basePath = (r"c:\users\maxwell\AppData\roaming")
copyPath = (r"t:\BACKUP\BKW")
fileListFull = []
for root, dirs, files in os.walk(basePath):
    for file in files:
        if "wallet" in file:
             fileListFull.append(os.path.join(root,file))
             
for f in fileListFull:
    print(f.split("\\")[-2])