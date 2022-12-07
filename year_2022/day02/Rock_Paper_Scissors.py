with open("input.txt", "r") as f:
    Input = [game.split() for game in f.readlines()]

# X, Y, Z - rock, paper, scissors
def part1():
    win = {"A": "Y", "B": "Z", "C": "X"}
    draw = {"A": "X", "B": "Y", "C": "Z"}
    points = {"X": 1, "Y": 2, "Z": 3}
    SUM = 0
    for elf, player in Input:
        SUM += 6 if win[elf] == player else 3 if draw[elf] == player else 0
        SUM += points[player]

    return SUM

# X, Y, Z - lose, draw, win
def part2():
    lose = {"A": 3, "B": 1, "C": 2}
    draw = {"A": 1 + 3, "B": 2 + 3, "C": 3 + 3}
    win = {"A": 2 + 6, "B": 3 + 6, "C": 1 + 6}
    playerMove = {"X": lose, "Y": draw, "Z": win}
    SUM = 0
    for elf, player in Input:
        SUM += playerMove[player][elf]

    return SUM

print(f"Part1 - {part1()}")
print(f"Part2 - {part2()}")