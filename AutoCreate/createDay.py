import os, sys, datetime, requests, re

date = datetime.date.today()
year = date.year
month = date.month
day = date.day

autoCreateLocation = __file__[:__file__.rindex("\\")] + "\\"

if len(sys.argv) != 2: 
    print(f"Not enough arguments! (PROGRAM, DAY_NUMBER)")
    sys.exit()

argDay = int(sys.argv[1])

if 1 > argDay or argDay > 25:
    print("Day is invalid! (from 1 to 25)")
    sys.exit()

folderYear = os.getcwd()[-4:]
# if it is december dont allow to create unreleased puzzles
if year == int(folderYear) and month == 12 and argDay > day:
    print(f"Puzzle from day {argDay} is not yet released! It's just December {day}")
    sys.exit()

if f"year_{folderYear}" not in os.getcwd():
    print("Not called from a year folder!")
    sys.exit()

dayPath = f"{os.getcwd()}\\day{argDay:{0}{2}}" # pad 0 to make the int always length of 2

if os.path.exists(dayPath):
    print("Day already exists!")
    sys.exit()

template = open(autoCreateLocation + "\\template.py", "r").read()
os.mkdir(dayPath)

# input
open((f"{dayPath}\\input.txt"), "w") # TODO fetch input from web based on day

# test
#open((f"{dayPath}\\test.txt"), "w")

# find the name on the web then request page. Then remove the edges then split the title and choose just the name
webContent = requests.get(f"https://adventofcode.com/{folderYear}/day/{argDay}").text
title = re.compile("<h2>.+<\/h2>").findall(webContent)[0][8:-9].split(": ")[1].replace(" ", "_")

open((f"{dayPath}\\{title}.py"), "w").write(template) # TODO fetch name from web