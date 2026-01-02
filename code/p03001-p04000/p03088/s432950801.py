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


def is_ok(s: str, c: str):
    if (s[1:3] == "AG"\
      or s[1:3] == "GA"\
      or (s[0:1] == "A" and s[2:3] == "G")\
      or s[0:2] == "AG")\
      and c == "C":
        return False

    elif s[1:3] == "AC" and c == "G":
        return False

    else:
        return True

from collections import defaultdict

n = ni()

dic = defaultdict(int)
dic["xxx"] = 1

atcg = "ATCG"
MOD = 10**9 + 7

for i in range(n):
    new_dic = defaultdict(int)
    for key, val in dic.items():
        for ci in atcg:
            if is_ok(key, ci):
                new_dic[key[1:] + ci] += val
                new_dic[key[1:] + ci] %= MOD

    dic = new_dic

ans = 0

for _, val in dic.items():
    ans += val
    ans %= MOD

print(ans)
