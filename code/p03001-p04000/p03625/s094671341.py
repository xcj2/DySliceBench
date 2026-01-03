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
a = list(li())

cnt = Counter(a)

first = 0
second = 0

keys = list(cnt.keys())
keys.sort(reverse=True)

for k in keys:
    if first != 0 and second != 0:
        break
    
    if first == 0 and second == 0 and cnt[k] >= 4:
        first = k
        second = k
        
    elif first != 0 and cnt[k] >= 2:
        second = k
        
    elif cnt[k] >= 2:
        first = k
        
print(first * second)