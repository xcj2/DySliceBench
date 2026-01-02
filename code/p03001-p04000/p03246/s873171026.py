import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import Counter

n = ni()
a = list(li())

even = Counter(a[::2])
odd = Counter(a[1::2])

es = even.most_common(2)
os = odd.most_common(2)

es = es + [(0,0)]
os = os + [(0,0)]

if es[0][0] != os[0][0]:
    print((n//2-es[0][1]) + (n//2-os[0][1]))
else:
    print(min((n//2-es[1][1]) + (n//2-os[0][1]),
              (n//2-es[0][1]) + (n//2-os[1][1])))