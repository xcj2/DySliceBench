import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**8) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import Counter

s = ns()
cnt = Counter()

for si in s:
    cnt[si] += 1
    
print('No')  if (cnt['N'] > 0 and cnt['S'] == 0) or\
                (cnt['N'] == 0 and cnt['S'] > 0) or\
                (cnt['E'] > 0 and cnt['W'] == 0) or\
                (cnt['E'] == 0 and cnt['W'] > 0) else print('Yes')
    