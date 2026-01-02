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
dic = defaultdict(int)

for _ in range(n):
    s = ns()
    cnts = [0]*26
    for si in s:
        cnts[ord(si)-ord('a')] += 1

    dic[tuple(cnts)] += 1

ans = 0
for _, v in dic.items():
    ans += v*(v-1) // 2

print(ans)

