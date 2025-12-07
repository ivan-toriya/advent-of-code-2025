from pathlib import Path


def parse_input(filename: str):
    inp = (Path(__file__).parent / filename).read_text()
    return inp.splitlines()


# === Part 1 ===


def part1(manifold: list[str]):
    beams = [{manifold[0].index("S")}]
    n_splits = 0

    for i in range(0, len(manifold) - 1):
        beams.append(set())  # next fold

        for b in beams[i]:
            match manifold[i + 1][b]:
                case ".":
                    beams[i + 1].add(b)
                case "^":
                    beams[i + 1].add(b - 1)
                    beams[i + 1].add(b + 1)
                    n_splits += 1
                case _:
                    raise NotImplementedError("Are you sure you're traveling through tachyon manifolds?")

    return n_splits


if __name__ == "__main__":
    manifold = parse_input("input.txt")
    print("Part 1: ", part1(manifold))
