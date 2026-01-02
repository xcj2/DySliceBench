from pprint import PrettyPrinter

pp = PrettyPrinter()


def read_tiles(h, w):
    c = []
    for _ in range(h):
        c.append([int(x) for x in input().split()])
    return c


def make_histogram(h, w, c):
    hg = [[None] * w for _ in range(h)]
    for j in range(w):
        hg[0][j] = 1 if c[0][j] == 0 else 0
    for i in range(1, h):
        for j in range(w):
            hg[i][j] = hg[i - 1][j] + 1 if c[i][j] == 0 else 0
    return hg


def largest_rectangle(h, w, c):
    lr = 0
    hg = make_histogram(h, w, c)
    # pp.pprint(hg)
    s = []
    for i in range(h):
        hg[i] += [0]
        for j in range(w + 1):
            if len(s) == 0:
                if hg[i][j] > 0:
                    s.append((hg[i][j], j))
            else:
                top = s[-1]
                if top[0] < hg[i][j]:
                    s.append((hg[i][j], j))
                elif hg[i][j] == top[0]:
                    pass
                else:
                    while len(s) > 0 and s[-1][0] >= hg[i][j]:
                        top = s.pop()
                        lr = max(lr, top[0] * (j - top[1]))
                    s.append((hg[i][j], top[1]))
            # print(j, lr, s)
    return lr


def main():
    h, w = map(int, input().split())
    c = read_tiles(h, w)
    print(largest_rectangle(h, w, c))


main()

