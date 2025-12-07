import math
import sys


def main():
    inp = sys.stdin.read()

    m = {}
    for y, line in enumerate(inp.split("\n")):
        for x, c in enumerate(line):
            m[(x, y)] = c
    w = max(x for x, y in m.keys()) + 1
    h = max(y for x, y in m.keys()) + 1

    # x position of first column in a group
    cols = [0] + [x + 1 for x in range(w) if all(m[(x, y)] == " " for y in range(h))]

    total1 = total2 = 0
    for s, e in zip(cols, cols[1:] + [w + 1]):
        f = sum if any(m[(x, h - 1)] == "+" for x in range(s, e - 1)) else math.prod
        total1 += f(
            int("".join(m[(x, y)] for x in range(s, e - 1))) for y in range(h - 1)
        )
        total2 += f(
            int("".join(m[(x, y)] for y in range(h - 1))) for x in range(s, e - 1)
        )

    print(1, total1)
    print(2, total2)


main()
