import json
import shutil
import os
import datetime

months = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}

inputPath = "/Volumes/SummerHDD/iPhonePics"
outputPath = "/Volumes/SummerHDD/Pics"
global totalCount 

def createLookUp():
    totalCount = 0
    lookup = {}
    for path, dirnames, filenames in os.walk(inputPath):
        for filename in filenames:
            totalCount += 1
            if filename == ".DS_Store":
                continue
            fullPath = f"{path}/{filename}"
            stat = os.lstat(fullPath)
            dateCreated = stat.st_mtime
            dateTime = datetime.datetime.fromtimestamp(dateCreated)  
            yearStr = str(dateTime.year)
            monthName = months[dateTime.month]
            # print(f"{filename}: {dateTime.year}-{monthName}")
            if yearStr not in lookup.keys():
                lookup[yearStr] = {}
            if monthName not in lookup[yearStr].keys():
                lookup[yearStr][monthName] = []
            lookup[yearStr][monthName].append(fullPath)
    return (lookup, totalCount)

def makeOutputDirs(lookup):
    for year in lookup.keys():
        yearPath = f"{outputPath}/{year}"
        os.mkdir(yearPath)
        for month in lookup[year].keys():
            monthPath = f"{yearPath}/{month}"
            os.mkdir(monthPath)

def copyFiles(lookup, totalCount):
    count = 0
    for year in lookup.keys():
        for month in lookup[year].keys():
            for src in lookup[year][month]:
                filename = src.split("/")[3]
                dest = f"{outputPath}/{year}/{month}/{filename}"
                shutil.copyfile(src, dest)
                count += 1
                print(f"{count}/{totalCount}: {(count/totalCount)*100}%")

    
def writeToFile(lookup):
    file = open("snapshot.json", "w")
    file.write(json.dumps(lookup, indent=4))

if __name__ == "__main__":
   lookup, totalCount = createLookUp() 
   writeToFile(lookup)
   makeOutputDirs(lookup)
   copyFiles(lookup, totalCount)
