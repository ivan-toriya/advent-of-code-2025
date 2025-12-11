from pathlib import Path


def parse_input(filename: str) -> dict[str, list[str]]:
    inp = (Path(__file__).parent / filename).read_text()
    result = {}
    for line in inp.splitlines():
        key, values = line.split(":", 1)
        result[key] = values.split()
    return result


def part1(devices: dict[str, list[str]]) -> int:
    to_check = devices["you"]
    count_out = 0

    while to_check:
        node = to_check.pop()

        if devices[node][0] == "out":
            count_out += 1
            continue

        to_check.extend(devices[node])

    return count_out


def part2(devices: dict[str, list[str]]) -> int:
    to_check = devices["svr"]
    count_out = 0

    dac_encountered = 0
    fft_encountered = 0
    dac_upstream = set()
    fft_upstream = set()

    # path = []

    while to_check:
        node = to_check.pop()
        # path.append(node)  # debug

        if devices[node][0] == "out":
            parents = [key for key, value in devices.items() if node in value]
            ...

            # Reset
            dac_encountered = 0
            fft_encountered = 0

            # path = []  # debug

            continue

        if dac_encountered:
            dac_upstream.add(node)
        elif fft_encountered:
            fft_upstream.add(node)

        if node == "dac":
            dac_encountered = 1
        elif node == "fft":
            fft_encountered = 1

        to_check.extend(devices[node])

    return count_out


if __name__ == "__main__":
    print("Part 1: ", part1(parse_input("input.txt")))
    # print("Part 2: ", part2(parse_input("sample2.txt")))
