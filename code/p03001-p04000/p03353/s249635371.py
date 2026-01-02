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

s = ns()
k = ni()

lens = len(s)

subset = set()

for i in range(len(s)):
    for j in range(1,k+1):
        subset.add(s[i:i+j])
        
sublist = sorted(list(subset))
print(sublist[k-1])