import sys


def main():
    line = sys.stdin.readline()
    ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in line.split(",")]
    s1 = 0
    for n in (n for (start, end) in ranges for n in range(start, end + 1)):
        n = str(n)
        if n[len(n) // 2 :] == n[: len(n) // 2]:
            s1 += int(n)
    print(s1)

    s2 = 0
    for n in (n for (start, end) in ranges for n in range(start, end + 1)):
        n = str(n)
        sublen = 1
        while sublen <= len(n) // 2:
            if len(n) % sublen != 0:
                sublen += 1
                continue
            first = n[:sublen]
            if all(
                n[i * sublen : (i + 1) * sublen] == first
                for i in range(len(n) // sublen)
            ):
                s2 += int(n)
                break
            sublen += 1
    print(s2)


main()
