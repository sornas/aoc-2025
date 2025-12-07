from collections import defaultdict
import sys


def show(splits, beams, timelines, w, h):
    for y in range(h):
        for x in range(w):
            if (x, y) in splits:
                print("^", end="")
            elif (x, y) in beams:
                print(timelines[(x, y)], end="")
            else:
                print(".", end="")
        print("")
    input()


def main():
    inp = open(sys.argv[1]).read()
    splits = set()
    for y, line in enumerate(inp.split("\n")):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == "^":
                splits.add((x, y))

    activated = set()
    timelines = defaultdict(lambda: 0, {start: 1})
    w = max(x for x, y in splits) + 1
    h = max(y for x, y in splits) + 1

    while True:
        # show(splits, beams, timelines, w + 1, h + 1)
        # O(för mycket)
        y = min(ty for tx, ty in timelines.keys())
        x = min(tx for tx, ty in timelines.keys() if ty == y)
        t = timelines.pop((x, y))
        if (x, y + 1) in splits:
            activated.add((x, y + 1))
            timelines[(x + 1, y + 1)] += t
            timelines[(x - 1, y + 1)] += t
        elif y + 1 > h:
            break
        else:
            timelines[(x, y + 1)] += t

    print(1, len(activated))
    print(2, sum(t for ((x, y), t) in timelines.items() if y == h))


main()
