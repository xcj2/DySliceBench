import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


from collections import defaultdict


def find_ans(dp, mod):
    nex = defaultdict(int)
    for key, val in dp.items():
        for c in ["A", "G", "C", "T"]:
            if (key[1:] == "AG" and c == "C")\
                or (key[1:] == "AC" and c == "G")\
                or (key[1:] == "GA" and c == "C")\
                or (key[:1] == "A" and key[2:] == "G" and c == "C")\
                or (key[:1] == "A" and key[1:2] == "G" and c == "C"):
                continue
            else:
                nex[key[1:] + c] += val
                nex[key[1:] + c] %= mod

    return nex

n = ni()
dp = defaultdict(int)
mod = 10**9 + 7

dp["TTT"] = 1

for _ in range(n):
    dp = find_ans(dp, mod)

ans = 0
for key, val in dp.items():
    ans += val
    ans %= mod

print(ans)