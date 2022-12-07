import os

template = open("template.py", "r").read()

print("This program will create folder with 25 days in it (solution, input and test files)")
folderName = input("folder_name: ")

yearPath = f"{os.getcwd()}\\{folderName}"
os.mkdir(yearPath)

for day in range(1, 25+1):
    dayPath = f"{yearPath}\\day_{day}"
    # day folder
    os.mkdir(dayPath)
    # input
    open((dayPath + "\\input.txt"), "w")
    # test
    open((dayPath + "\\test.txt"), "w")
    # py file
    open((dayPath + "\\" + str(day) + ".py"), "w").write(template)