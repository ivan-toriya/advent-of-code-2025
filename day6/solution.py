from math import prod
from pathlib import Path

input = (Path(__file__).parent / "sample.txt").read_text()


def safe_cast(x: str) -> int | str:
    try:
        return int(x)
    except ValueError:
        return x


def parse_input(string: str):
    """
    Converts

    ```
    123 328
     45 64
      6 98
    *   +
    ```

    Into

    ```
    [(123, 45, 6, "*"), (328, 64, 98, "+")]
    ```
    """
    return [s for s in zip(*[map(safe_cast, line.split()) for line in string.splitlines()])]


problems = parse_input(input)


grand_total = 0

for p in problems:
    match p[-1]:
        case "+":
            grand_total += sum(p[:-1])
        case "*":
            grand_total += prod(p[:-1])

print("Part 1: ", grand_total)


# === Part 2 ===


def parse_input_p2(string: str) -> list[list[tuple[str, ...]]]:
    """
    Converts

    ```
    883 741
    491 438
    132 241
    72  61
    *   +
    ```

    Into

    ```
    [
        [('8', '4', '1', '7', '*'), ('8', '9', '3', '2', ''), ('3', '1', '2', '', '')],
        [('7', '4', '2', '6', '+'), ('4', '3', '4', '1', ''), ('1', '8', '1', '', '')]
    ]
    ```
    """
    from itertools import groupby

    line = [line for line in string.splitlines()]
    transposed = list(zip(*line))
    stripped = [tuple(char.strip() for char in column) for column in transposed]

    DELIMITER = ("",) * len(stripped[0])

    return [list(group) for key, group in groupby(stripped, lambda x: x != DELIMITER) if key]


grand_total = 0
for problem in parse_input_p2(input):
    nums = []
    operation = None
    for i, column in enumerate(problem):
        if i == 0:
            *digits, operation = column
        else:
            *digits, _ = column

        nums.append(int("".join(digits)))

    match operation:
        case "+":
            grand_total += sum(nums)
        case "*":
            grand_total += prod(nums)


print("Part 2: ", grand_total)
