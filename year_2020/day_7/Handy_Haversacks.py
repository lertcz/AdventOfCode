with open('input.txt', 'r') as f:
    Input = [line.strip().split(" contain ") for line in f.readlines()]
    # split Input
    Input = [[line[0][:-4].strip(), line[1][:-1].split(", ")] for line in Input]
    # for each line add the source bag then add all childs and the quantity
    Input = [[bags[0], [[bag[0], (bag[2:])[:-4].strip()] for bag in bags[1]]] for bags in Input]

# create dictionary which will hold which bag hold what (part2)
bags_children = dict()
for bags in Input:
    bags_children[bags[0]] = bags[1] # bag key > bag children


# create dict which stores the origin of a given bag (part1)
bags_origin = dict()
for bags in Input:
    parent = bags[0]
    for child in bags[1]:
        if child[1] in bags_origin.keys():
            bags_origin[child[1]] += [parent]
        else:
            bags_origin[child[1]] = [parent]

def find_parents(bag):
    if bag in bags_origin.keys():
        for bags in bags_origin[bag]:
            found_bags.append(bags) if bags not in found_bags else None
            find_parents(bags)

def find_content(bag_name):
    if bags_children[bag_name][0][1] == "other":
        return 1
    
    count = 0
    for bag in bags_children[bag_name]: # add the contents of child times it's count
        count += find_content(bag[1]) * int(bag[0])
    
    print("bagname:", bag_name, ", count:", count)
    return count + 1 # return bags value + it self

found_bags = []
find_parents("shiny gold")
print("Part 1: The amount of different coloured bags that can hold a shiny gold bag:", len(found_bags))

print("Part2: The amount of different coloured bags that a shiny gold bag can gold:", find_content("shiny gold") - 1)