import sys


def main():
    tiles = [
        tuple(map(int, l.split(","))) for l in open(sys.argv[1]).read().split("\n") if l
    ]
    print(tiles)

    m_area = 0
    m_area_tiles = None
    for (x1, y1), (x2, y2) in (
        (p1, p2) for i, p1 in enumerate(tiles) for p2 in tiles[i + 1 :]
    ):
        area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
        if area > m_area:
            m_area = area
            m_aera_tiles = ((x1, y1), (x2, y2))
    print(m_area, m_aera_tiles)


main()
