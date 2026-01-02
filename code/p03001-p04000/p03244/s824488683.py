import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

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
v = list(li())

odd = Counter(v[::2])
even = Counter(v[1::2])

odd_cm = odd.most_common(2)
even_cm = even.most_common(2)

odd_cm.append((0,0))
even_cm.append((0,0))

if odd_cm[0][0] != even_cm[0][0]:
    print(n - odd_cm[0][1] - even_cm[0][1])
    
else:
    print(min(n - odd_cm[1][1] - even_cm[0][1],
              n - odd_cm[0][1] - even_cm[1][1]))