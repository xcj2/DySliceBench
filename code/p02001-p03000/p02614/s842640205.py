#!/usr/bin/env python3
import sys
import copy


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    H, W, K = MI()
    cells = []
    ans = 0
    for i in range(H):
        row = input()
        rows = []
        for item in range(len(row)):
            if row[item] == ".":
                rows.append(0)
            else:
                rows.append(1)
        cells.append(rows)

    for i in range(2**H):
        for j in range(2**W):
            iBi = format(i, '0'+str(H)+'b')
            jBi = format(j, '0'+str(W)+'b')

            tmp_cell = copy.deepcopy(cells)

            for ii in range(H):
                for jj in range(W):
                    if str(iBi)[ii] == '1' or str(jBi)[jj] == '1':

                        tmp_cell[ii][jj] = 0
            if sum(map(sum, tmp_cell)) == K:
                ans += 1

    print(ans)

    # oj t -c "pypy3 main.py"
    # acc s main.py -- --guess-python-interpreter pypy


main()
