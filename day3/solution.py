from pathlib import Path

input = Path("day3/input.txt").read_text()


total = 0

for bank in input.splitlines():
    combinations = set()
    previous = 0
    for idx, battery in enumerate(bank):
        if int(battery) <= previous or len(bank) == idx + 1:
            continue
        combinations.update((int(battery + b) for b in bank[idx + 1 :]))
        previous = int(battery)
    total += max(combinations)


print("Part 1: ", total)
