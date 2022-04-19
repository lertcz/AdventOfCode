with open("input.txt", "r") as f:
    input = [str(line).split() for line in f.readlines()]

valid = [0, 0]
for amount, char, password in input:
    amount = [int(num) for num in amount.split("-")]
    char = char[0]

    if amount[0] <= password.count(char) <= amount[1]:
        valid[0] += 1
    
    if (password[amount[0] - 1] == char) ^ (password[amount[1] - 1] == char): # only if the values are true and false
        valid[1] += 1

print("part1:", valid[0])
print("part2:", valid[1])