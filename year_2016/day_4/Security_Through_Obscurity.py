from collections import Counter

with open('input.txt', 'r') as f:
    Input = [id.strip() for id in f.readlines()]
    rooms = []
    validRooms = []
    for room in Input:
        checksum = room[room.rfind('[')+1:-1]
        room = room[:room.rfind('[')]
        id = room[room.rfind('-')+1:]
        name = ''.join(room[:room.rfind('-')].split('-'))
        wholename = room[:room.rfind('-')]
        rooms.append([name, id, checksum])
        validRooms.append([wholename, id])

def overall_top5_occurrence(occurrence):
    boundary = occurrence[4][1]
    string = ""
    # sort characters into groups of most occurred
    for i in range(occurrence[0][1], boundary-1, -1):
        temp = []
        for char, occ in occurrence:
            if occ == i:
                temp.append(char)
        # sort and add to string
        string += "".join(sorted(temp))

    return string

def part1():
    global validRooms
    valid = 0
    part2_data = []
    for i, data in enumerate(rooms):
        name, id, checksum = data
        occurrence = overall_top5_occurrence(Counter(name).most_common())

        # if first 5 chars in occurrance match checksum add id to total
        if occurrence[:5] == checksum:
            part2_data.append(i)
            valid += int(id)

    for i in range(len(rooms)-1, -1, -1):
        if i not in part2_data:
            validRooms.pop(i)

    return valid

def part2():
    for name, id in validRooms:
        name = name.replace("-", " ")
        increment = int(id) % 26
        newName = ""
        for char in name:
            #97 122  a-z
            ascii = ord(char) - 96
            if ascii != ord(" ") - 96:
                ascii += increment
                ascii %= 26
                newName += chr(ascii + 96)
            else:
                newName += " "
            
        
        if "north" in newName:
            return id

if __name__ == "__main__":
    print(f"Part1: number of valid numbers is: {part1()}")
    print(f"Part2: North Pole objects are stored in room with id: {part2()}")