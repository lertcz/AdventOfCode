with open('input.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]

answer = 0
missing = []
for boardingPass in input:
    row = [0, 127]
    for side in boardingPass[:7]:
        if side == 'F':
            row[1] = sum(row) // 2
        else:
            row[0] = sum(row) // 2 +1

    col = [0, 7]
    for side in boardingPass[-3:]:
        if side == 'L':
            col[1] = sum(col) // 2
        else:
            col[0] = sum(col) // 2 +1

    if row[0] != 0 or 127:
        id = row[0] * 8 + col[0]
        missing.append(id)
        if answer < id:
            answer = id

print(answer)

missing = sorted(missing)

x=6
for i, id in enumerate(missing):
    if i+6 != id:
        print(id-1)
        break