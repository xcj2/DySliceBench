import sys
from itertools import accumulate, combinations

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


H, W, K = MI()
S = [[int(x) for x in list(input())] for _ in range(H)]


def fn(bits):
    slice = 0
    n = bin(bits).count("1")
    block_cnts = [0] * n
    for j in range(W):
        sec = 0
        col_cnts = [0] * n
        for i in range(H):
            col_cnts[sec] += S[i][j]
            if col_cnts[sec] > K:
                return -1
            if (bits >> i) & 1:
                sec += 1
        if all(block_cnts[sec] + col_cnts[sec] <= K for sec in range(n)):
            for sec in range(n):
                block_cnts[sec] += col_cnts[sec]
        else:
            slice += 1
            block_cnts = col_cnts
    return slice


ans = INF
for bits in range(1 << (H - 1)):
    hslice = bin(bits).count("1")
    wslice = fn(bits + (1 << (H - 1)))
    if wslice > -1:
        ans = min(ans, hslice + wslice)
print(ans)
