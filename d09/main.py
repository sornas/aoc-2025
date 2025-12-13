from collections import defaultdict
from itertools import chain
import sys


def show(
    horizontal: dict[int, tuple[int, int]],
    vertical: dict[int, tuple[int, int]],
    p1x,
    p1y,
    p2x,
    p2y,
):
    print(vertical)
    print(horizontal)
    for y in range(9):
        for x in range(14):
            if p1x <= x <= p2x and p1y <= y <= p2y:
                print("#", end="")
                continue
            corner = False
            tile = False
            for hy, hx in horizontal.items():
                for hx1, hx2 in hx:
                    if y != hy:
                        break
                    elif x == hx1 or x == hx2:
                        corner |= True
                    elif hx1 <= x <= hx2:
                        tile |= True
            for hx, hy in vertical.items():
                for hy1, hy2 in hy:
                    if x != hx:
                        break
                    elif y == hy1 or y == hy2:
                        corner |= True
                    elif hy1 <= y <= hy2:
                        tile |= True
            if corner:
                print("x", end="")
            elif tile:
                print("o", end="")
            else:
                print(".", end="")
        print()


def main():
    tiles = [
        tuple(map(int, l.split(","))) for l in open(sys.argv[1]).read().split("\n") if l
    ]

    areas = []
    for (x1, y1), (x2, y2) in (
        (p1, p2) for i, p1 in enumerate(tiles) for p2 in tiles[i + 1 :]
    ):
        area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
        areas.append((area, (x1, y1), (x2, y2)))
    areas.sort()
    print(1, areas[-1][0])

    horizontal = defaultdict(list)
    vertical = defaultdict(list)
    for (t1x, t1y), (t2x, t2y) in zip(tiles, tiles[1:] + [tiles[0]]):
        if t1x == t2x:
            vertical[t1x].append((min(t1y, t2y), max(t1y, t2y)))
        else:
            horizontal[t1y].append((min(t1x, t2x), max(t1x, t2x)))

    for l in chain(horizontal.values(), vertical.values()):
        l.sort()

    show(horizontal, vertical, 0, 0, 0, 0)

    for _, (x1, y1), (x2, y2) in reversed(areas):
        ...


main()
