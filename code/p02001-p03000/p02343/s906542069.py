#!python3

import sys
iim = lambda: map(int, input().rstrip().split())

def resolve():
    N, Q = iim()

    S = [[i] for i in range(N)]

    def find(i):
        x = S[i]
        while True:
            k = S[i][0]
            if k == i:
                x[0] = i
                return i
            S[i] = x
            i = k
    def union(i, j):
        ai = find(i)
        aj = find(j)
        if ai != aj:
            S[aj][0] = S[ai][0]
            S[aj] = S[ai]

    def same(i, j):
        ai = find(i)
        aj = find(j)
        return ai == aj

    ans = []
    for com, x, y in (map(int, line.split()) for line in sys.stdin):

        if com == 0:
            union(x, y)
            #print(x, y, *tuple(map(lambda x: (x, hex(id(x))[-4:]), S)))
        elif com == 1:
            ans.append(1 if same(x, y) else 0)
        else:
            raise 1
    print(*ans, sep="\n")


if __name__ == "__main__":
    resolve()

