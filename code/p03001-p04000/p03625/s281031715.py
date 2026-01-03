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

cnt = Counter(a)

lst = []
for k,v in cnt.items():
    lst.append((k,v))

lst.sort(reverse=True)

first = 0
second = 0

for k,v in lst:
    if v >= 4 and first == 0:
        first = k
        second = k
        break
    
    elif v >= 4:
        second = k
        break
        
    elif v >= 2 and first != 0:
        second = k
        break
    
    elif v >= 2:
        first = k
        
print(first*second)