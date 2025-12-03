import sys


def main():
    inp = sys.stdin.readlines()
    s1 = 0
    for line in inp:
        bank = list(map(int, (x for x in line.strip())))
        n1 = max(bank[:-1])
        i = bank.index(n1)
        n2 = max(bank[i + 1 :])
        s1 += n1 * 10 + n2
    print(s1)

    s2 = 0
    for line in inp:
        bank = list(map(int, (x for x in line.strip())))
        joltage = 0
        offset = 0
        for n in range(12):
            max_end = -(12 - n - 1)
            if max_end == 0:
                max_end = len(bank)
            jolt = max(bank[offset:max_end])
            offset = offset + bank[offset:max_end].index(jolt) + 1
            joltage += jolt * 10 ** (11 - n)
        s2 += joltage
    print(s2)


main()
