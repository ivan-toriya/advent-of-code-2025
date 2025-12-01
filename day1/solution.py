import re
from pathlib import Path

input = Path("day1/input.txt").read_text().splitlines()


def parse_input(input: list[str]) -> list[tuple[str, int, int]]:
    pattern = re.compile(r"^(L|R)(\d*?)(\d{1,2})$")
    output = []
    for i in input:
        m = re.search(pattern, i)
        if m:
            output.append((m.group(1), int(m.group(2) or 0), int(m.group(3))))
    return output


# Part 1
DIAL = [n for n in range(100)]

position = DIAL[50]
total = 0

for direction, _, n in parse_input(input):
    match direction:
        case "L":
            position -= n
            if position < 0:
                position += 100
        case "R":
            position += n
            if position > 99:
                position -= 100
    if position == 0:
        total += 1
    # print(direction, n, position)

print("Part 1: ", total)

# Part 2
DIAL = [n for n in range(100)]

position = DIAL[50]
total = 0

for direction, times, n in parse_input(input):
    print(direction, n, position, total)
    match direction:
        case "L":
            if position == 0:
                position -= n
                position += 100
            else:
                position -= n
                if position < 0:
                    total += 1
                    position += 100
        case "R":
            position += n
            if position > 100:
                total += 1
            if position > 99:
                position -= 100
    if position == 0:
        total += 1
    total += times

print("Part 2: ", total)
