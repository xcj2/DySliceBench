# coding: utf-8

II = lambda: int(input())
MI = lambda: map(int, input().split())


def make_cells(h, w):
    cells = set()
    for i in range(h):
        for j in range(w):
            cells.add((i, j))
    return cells

def make_bcells(h, w, m):
    cells = set()
    for i in range(h):
        for j in range(w):
            if m[i][j]:
                cells.add((i, j))
    return cells


def search(sc, bcells_yet, m, H, W):
    valid = lambda cell: cell[0] >= 0 and cell[0] < H and cell[1] >= 0 and cell[1] < W
    color = lambda cell: m[cell[0]][cell[1]]

    ccnt = {0:0, 1:1}
    wcells_searched = set()

    q = set()
    q.add(sc)
    while len(q) > 0:
        c = q.pop()
        dirs = filter(valid, [(c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1)])
        for nc in dirs:
            if color(nc) != color(c):
                if color(nc) and nc in bcells_yet:
                    bcells_yet.remove(nc)
                    ccnt[1] += 1
                    q.add(nc)
                elif not color(nc) and nc not in wcells_searched:
                    wcells_searched.add(nc)
                    ccnt[0] += 1
                    q.add(nc)
    return ccnt[0] * ccnt[1]


def main():
    H, W = MI()

    m = []
    for h in range(H):
        m.append(tuple(map(lambda c:c == "#", input())))

    bcells = make_bcells(H, W, m)

    ans = 0
    while len(bcells) > 0:
        ans += search(bcells.pop(), bcells, m, H, W)
    return ans


if __name__ == "__main__":
    print(main())
