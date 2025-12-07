from collections import deque, defaultdict
import sys


def show(splits, beams, w, h):

    for y in range(h):
        for x in range(w):
            if (x, y) in splits:
                print("^", end="")
            elif (x, y) in beams:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    input()


def main():
    inp = open(sys.argv[1]).read()
    splits = set()
    activated = set()
    for y, line in enumerate(inp.split("\n")):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == "^":
                splits.add((x, y))
    max_y = max(y for x, y in splits)
    beams = deque([start])
    w = max(x for x, y in splits)
    h = max(y for x, y in splits)

    while beams:
        # show(splits, beams, 5, 5)
        (x, y) = beams.popleft()
        if (x, y + 1) in splits:
            activated.add((x, y + 1))
            if (x + 1, y + 1) not in beams:
                beams.append((x + 1, y + 1))
            if (x - 1, y + 1) not in beams:
                beams.append((x - 1, y + 1))
        elif y > max_y + 10:
            pass
        else:
            beams.append((x, y + 1))
    print(len(activated))


def main2():
    inp = open(sys.argv[1]).read()
    splits = set()
    activated = set()
    for y, line in enumerate(inp.split("\n")):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == "^":
                splits.add((x, y))
    max_y = max(y for x, y in splits)
    beams = deque([start])
    timelines = defaultdict(lambda: 0)
    timelines[start] = 1
    w = max(x for x, y in splits)
    h = max(y for x, y in splits)

    while beams:
        (x, y) = beams.popleft()
        t = timelines[(x, y)]
        if (x, y + 1) in splits:
            timelines[(x + 1, y + 1)] += t
            timelines[(x - 1, y + 1)] += t
            if (x + 1, y + 1) not in beams:
                beams.append((x + 1, y + 1))
            if (x - 1, y + 1) not in beams:
                beams.append((x - 1, y + 1))
        elif y > max_y + 10:
            pass
        else:
            timelines[(x, y + 1)] += t
            beams.append((x, y + 1))
    print(sum(t for ((x, y), t) in timelines.items() if y == max_y + 1))


main2()
