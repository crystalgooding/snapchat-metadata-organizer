#
# 
# Info on Shutil library:
# https://docs.python.org/3/library/shutil.html
# 
#  cd file
#  py script.py
# 
# 
# 
# #


import os
import re
import shutil
from pathlib import Path

import piexif
from mutagen.mp4 import MP4

source = Path('.') # input directory
outputdir = source / 'out' # output directory

outputdir.mkdir(exist_ok=True) #make the folder


dateMatcher = re.compile(r'^(?P<date>\d{4}-\d{2}-\d{2})_') #grabs the dates from the name

def fixJPG(OGpath: Path, date: str):
    dst_path = outputdir / OGpath.name #builds the output path by combining the outp directory with the original file name
    shutil.copy2(OGpath, dst_path) #copies the original .jpg into the outp folder.
 
    matadata = piexif.load(str(dst_path))  #reads all the existing metadata from the copied file into a dictionary
    finalData = date.replace('-', ':') + " 00:00:00" #the time is fixed to midnight since only the date comes from the filename
    matadata["Exif"][piexif.ExifIFD.DateTimeOriginal] = finalData.encode('utf-8') #updates when the photo was taken
    
    exif_bytes = piexif.dump(matadata) #converts the updated dict back into raw exif
    piexif.insert(exif_bytes, str(dst_path)) #shoves it back into the data

    #output for when the conversion is done, for debugging
    message = "[JPEG]  " + OGpath.name + " → out/" + dst_path.name + \
          " (DateTimeOriginal=" + finalData + ")"
    print(message)

def fixMP4(OGpath: Path, date: str):
    dst_path = outputdir / OGpath.name #build destimation path
    shutil.copy2(OGpath, dst_path) #copy over to new folder
    
    mp4file = MP4(str(dst_path)) #read in file to edit

    mp4file["\xa9day"] = [date] #metadata key that stores the creation/release date
    mp4file.save()

    #output for when its done
    message = "[MP4]   " + OGpath.name + " → out/" + dst_path.name + \
          " (©day=" + date + ")"
    print(message)

def main():
    for entry in source.iterdir():
        if not entry.is_file():
            continue
        
        if entry.suffix.lower() not in ('.jpeg', '.jpg', '.mp4'): #if its not the right file, skip
            continue
        
        m = dateMatcher.match(entry.name)
        if not m:
            print("[SKIP]  filename does not match pattern: " + entry.name)
            continue
        
        date = m.group('date')
        
        #I already check if its a jpeg or mp4, this is just for which one to call
        if entry.suffix.lower() in ('.jpg', '.jpeg'):
            fixJPG(entry, date)
        else:
            fixMP4(entry, date)

if __name__ == "__main__":
    main()
