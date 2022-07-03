import os 

# Helper script to check where the files are, not used in main program

inputPath = "/Volumes/SummerHDD/Pics"

for path, dirnames, filenames in os.walk(inputPath):
    if len(filenames) > 0:
        print(f"{path}: {filenames}")
