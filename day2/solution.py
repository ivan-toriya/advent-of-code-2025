from pathlib import Path

input = Path("day2/input.txt").read_text()

ranges = [list(map(int, r.split("-"))) for r in input.split(",")]

# === PART 1 ===

invalid_ids = []
for r in ranges:
    for id in range(r[0], r[1] + 1):
        _id = str(id)
        if (length := len(_id)) % 2 == 1:
            # we can't split in half,
            continue
        left, right = _id[: length // 2], _id[length // 2 :]
        if left == right:
            invalid_ids.append(id)

print("Part 1: ", sum(invalid_ids))
