import re
import sys
from collections import defaultdict


def non_overlap(candidate, overlay):
    c1, c2 = candidate
    o1, o2 = overlay


def main():
    inp = sys.stdin.read()

    # parsing
    fresh_inp, avail_inp = inp.split("\n\n")
    fresh = []
    for l in fresh_inp.split("\n"):
        m = re.match(r"(\d+)-(\d+)", l)
        fresh.append((int(m.group(1)), int(m.group(2))))

    # part 1
    num_fresh = 0
    for l in avail_inp.split("\n"):
        if not l.strip():
            continue
        ingr = int(l)
        for s, e in fresh:
            if ingr in range(s, e + 1):
                num_fresh += 1
                break
    print(1, num_fresh)

    # part 2
    total = 0
    for i, (a1, a2) in enumerate(fresh):
        ranges = [(a1, a2)]
        for o1, o2 in fresh[i + 1 :]:
            new_ranges = []
            for c1, c2 in ranges:
                if o2 < c1:
                    new_ranges += [(c1, c2)]
                elif o1 > c2:
                    new_ranges += [(c1, c2)]
                elif o1 > c1 and o2 < c2:
                    new_ranges += [(c1, o1 - 1), (o2 + 1, c2)]
                elif o1 > c1 and o2 >= c2:
                    new_ranges += [(c1, o1 - 1)]
                elif o1 <= c1 and o2 < c2:
                    new_ranges += [(o2 + 1, c2)]
                elif o1 <= c1 and o2 >= c2:
                    pass
                else:
                    assert False
            ranges = new_ranges
        for s, e in ranges:
            total += e - s + 1
    print(2, total)

    # part 2 (B2)
    stops = defaultdict(lambda: 0)
    for s, e in fresh:
        stops[s] += 1
        stops[e] -= 1
    cur = 0
    total = 0
    for n, step in sorted(stops.items()):
        if cur == 0:
            start = n
        cur += step
        if cur == 0:
            total += n - start + 1
    print(2, total)


main()
