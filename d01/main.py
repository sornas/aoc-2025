import sys

def part1():
    dial = 50
    s = 0
    for line in sys.stdin:
        d = line[0]
        amount = int(line[1:])
        dial = (dial + (1 if d == "R" else -1) * amount) % 100
        if dial == 0:
            s += 1
    print(s)

def part2():
    dial1 = 50
    dial2 = 50
    s1 = 0
    s2 = 0
    # print("dir", "amont", "start", "end", "dial", "delta", "before", "after", sep='\t')
    for line in sys.stdin:
        d = line[0]
        amount1 = int(line[1:])
        amount2 = int(line[1:])
        sign = 1 if d == "R" else -1
        while amount1 > 0:
            dial1 += sign
            if dial1 % 100 == 0:
                s1 += 1
            amount1 -= 1

        end = (dial2 + sign * amount2)
        dial2 = end
        before = s2
        if dial2 == 0:
            s2 += 1
        while dial2 < 0:
            dial2 += 100
            s2 += 1
        while dial2 > 99:
            dial2 -= 100
            s2 += 1
        after = s2

    print(s1, s2)

part2()
