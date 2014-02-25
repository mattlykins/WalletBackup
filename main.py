import os
import shutil
import subprocess as sp
basePath = (r"c:\users\maxwell\AppData\roaming")
copyPath = (r"t:\BACKUP\BKW")
zipPath = (r"C:\Program Files\7-Zip\7z.exe")
password = "archivePassword"
if not os.path.exists(copyPath):
    os.makedirs(copyPath)
    
fileListFull = []
outputBase = []
for root, dirs, files in os.walk(basePath):
    for file in files:
        if "wallet" in file:
            fileListFull.append(os.path.join(root,file))
             
for f in fileListFull:
    outputBase.append(f.split("\\")[-2])
    
for copyFrom,copyTo in zip(fileListFull,outputBase):
#    shutil.copyfile(copyFrom,copyPath+"\\"+copyTo+".dat")
    rc=sp.call([zipPath, 'a', "-p"+password, '-y', copyPath+"\\"+copyTo+".7z"] + [copyFrom])
