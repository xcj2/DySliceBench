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

n = ni()
a = list(li())

dic = defaultdict(int)

for ai in a:
    dic[ai] += 1

ans = 0
evn = 0

for _, cnt in dic.items():
    if cnt % 2:
        ans += 1

    else:
        evn += 1

        if evn == 2:
            ans += 2
            evn = 0

print(ans)