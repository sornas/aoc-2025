import re
import sys


def non_overlap(candidate, overlay):
    c1, c2 = candidate
    o1, o2 = overlay
    if o2 < c1:
        return [(c1, c2)]
    elif o1 > c2:
        return [(c1, c2)]
    elif o1 > c1 and o2 < c2:
        return [(c1, o1 - 1), (o2 + 1, c2)]
    elif o1 > c1 and o2 >= c2:
        return [(c1, o1 - 1)]
    elif o1 <= c1 and o2 < c2:
        return [(o2 + 1, c2)]
    elif o1 <= c1 and o2 >= c2:
        return []
    else:
        assert False


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

    # part 2
    total = 0
    for i, (a1, a2) in enumerate(fresh):
        ranges = [(a1, a2)]
        for b1, b2 in fresh[i + 1 :]:
            new_ranges = []
            for c1, c2 in ranges:
                new_ranges += non_overlap((c1, c2), (b1, b2))
            ranges = new_ranges
        for s, e in ranges:
            total += e - s + 1
    print(total)


main()
