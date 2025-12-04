import sys


def ns(x, y, w, h):
    return (
        (x + dx, y + dy)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if (dx, dy) != (0, 0)
        and x + dx >= 0
        and y + dy >= 0
        and x + dx < w
        and y + dy < h
    )


def main():
    inp = sys.stdin.readlines()
    paper = set()
    empty = set()
    for y, line in enumerate(inp):
        line = line.strip()
        for x, c in enumerate(line):
            if c == "@":
                paper.add((x, y))
            else:
                empty.add((x, y))
    w = len(inp[0].strip())
    h = len(inp)
    s1 = 0
    for x, y in paper:
        adj = set()
        for n in ns(x, y, w, h):
            if n in paper:
                adj.add(n)
        if len(adj) < 4:
            s1 += 1
    print(s1)


def main2():
    inp = sys.stdin.readlines()
    paper = set()
    empty = set()
    for y, line in enumerate(inp):
        line = line.strip()
        for x, c in enumerate(line):
            if c == "@":
                paper.add((x, y))
            else:
                empty.add((x, y))
    w = len(inp[0].strip())
    h = len(inp)
    before = len(paper)
    while True:
        remove = []
        for x, y in paper:
            adj = set()
            for n in ns(x, y, w, h):
                if n in paper:
                    adj.add(n)
            if len(adj) < 4:
                remove.append((x, y))
        if len(remove) == 0:
            break
        for p in remove:
            paper.remove(p)
    print(before - len(paper))


main2()
