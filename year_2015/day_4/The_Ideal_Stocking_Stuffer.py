import hashlib

Input = b"yzbqklnj" # value

def part1():
    x = 0
    while True:
        key = str(x).encode()
        result = hashlib.md5(Input+key).hexdigest()
        if result[:5] == "00000":
            return x
        
        x += 1
        


def part2(): # loooong
    x = 0
    while True:
        key = str(x).encode()
        result = hashlib.md5(Input+key).hexdigest()
        if result[:6] == "000000":
            return x
        
        x += 1

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")