from collections import defaultdict
import math
import sys


def dist(bb1, bb2):
    return sum((b1 - b2) ** 2 for b1, b2 in zip(bb1, bb2))


def main():
    inp = open(sys.argv[1]).read().split("\n")
    boxes = [tuple(map(int, l.split(","))) for l in inp if l]

    pairs = list(
        reversed(
            sorted(
                (dist(b1, b2), b1, b2)
                for i, b1 in enumerate(boxes)
                for b2 in boxes[i + 1 :]
            )
        )
    )

    parent = {b: b for b in boxes}
    connections = 0

    def find(b):
        if parent[b] != b:
            parent[b] = find(parent[b])
            return parent[b]
        return b

    def union(b1, b2):
        nonlocal connections
        b1 = find(b1)
        b2 = find(b2)

        if b1 != b2:
            connections += 1
            parent[b2] = b1

    def get_circuits(boxes):
        circuits = defaultdict(list)
        for b in boxes:
            circuits[find(b)].append(b)

        circuit_lens = [(len(c), b) for b, c in circuits.items()]
        circuit_lens.sort()

        return circuits, circuit_lens

    def show(boxes):
        c, cl = get_circuits(boxes)
        for l, b in cl:
            print(l, b, "\t", list(sorted(c[b])))

    c = 0
    while connections != 999:
        d, b1, b2 = pairs.pop()
        # print("#" * 100)
        # print(c)
        # print(f"{b1} -> {b2}")
        union(b1, b2)
        # show(boxes)

    print(b1[0] * b2[0])
    c, cl = get_circuits(boxes)
    print(math.prod(l for l, _ in cl[-3:]))


main()
