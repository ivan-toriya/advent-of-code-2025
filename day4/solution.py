from pathlib import Path

input = Path("day4/input.txt").read_text()

GRID = input.splitlines()
HEIGHT = len(GRID)
WIDTH = len(GRID[0])

POSITIONS = ((-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1))


# === Part 1 ===


def is_accessible(y: int, x: int, grid: list[str]) -> bool:
    neighbours = 0
    for dy, dx in POSITIONS:
        py, px = dy + y, dx + x

        if py < 0 or py >= HEIGHT or px < 0 or px >= WIDTH:
            continue

        neighbours += grid[py][px] == "@"
        if neighbours == 4:
            return False
    return True


def part1():
    total = 0
    for y, row in enumerate(GRID):
        for x, cell in enumerate(row):
            if cell == "@":
                total += is_accessible(y, x, GRID)
    return total


print("Part 1: ", part1())

# === Part 2 ===

removed = set()


def is_accessible_and_not_removed(y: int, x: int, grid: list[str]) -> bool:
    neighbours = 0
    for dy, dx in POSITIONS:
        py, px = dy + y, dx + x

        if py < 0 or py >= HEIGHT or px < 0 or px >= WIDTH:
            continue

        if grid[py][px] == "@" and (py, px) not in removed:
            neighbours += 1

        if neighbours == 4:
            return False
    return True


def part2() -> int:
    while True:
        n_removed = 0
        for y, row in enumerate(GRID):
            for x, cell in enumerate(row):
                if cell == "@":
                    if (y, x) in removed:
                        continue
                    if is_accessible_and_not_removed(y, x, GRID):
                        removed.add((y, x))
                        n_removed += 1

        if n_removed == 0:
            break

    return len(removed)


print("Part 2: ", part2())
