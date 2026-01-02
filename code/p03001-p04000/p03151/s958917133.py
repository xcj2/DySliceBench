import sys
import io
import numpy as np
import itertools

def parse(inp):
    N=int(next(inp).split()[0])
    A=np.array(next(inp).split(),dtype=int)
    B=np.array(next(inp).split(),dtype=int)
    return N,A,B


def magic(D):
    moved = sum(D < 0)
    if (moved == 0): return 0
    s_minus = sum(D[D < 0])

    pluslist = np.sort(D[D > 0])[::-1]

    for i in itertools.accumulate(pluslist):
        moved += 1
        if (i > abs(s_minus)):
            break

    return moved


def main(inp):
    N = inp[0]
    A = inp[1]
    B = inp[2]
    D = np.empty(N, dtype=int)
    for i in range(N):
        D[i] = A[i] - B[i]

    if (A.sum() < B.sum()):
        return -1
    else:
        return magic(D)


print(main(parse(sys.stdin)))

