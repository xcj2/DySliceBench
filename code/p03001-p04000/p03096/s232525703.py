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

from collections import Counter, defaultdict

def compress(c: list) -> list:
    pre = 0
    ret = []
    for ci in c:
        if ci != pre:
            ret.append(ci)
            
        pre = ci
        
    return ret

def rem_alone(c: list) -> list:
    cnt = Counter(c)
    aln = set()
    for k, v in cnt.items():
        if v == 1:
            aln.add(k)
        
    ret = []
    for ci in c:
        if ci in aln:
            continue
        
        ret.append(ci)
        
    return ret

def find_prev_idx(c: list) -> dict:
    idx = defaultdict(list)
    prev = defaultdict(int)
    for i, ci in enumerate(c):
        prev[i+1] = idx[ci][-1] if len(idx[ci]) > 0 else -1
        idx[ci].append(i+1)

    
    return prev
 
n = ni()
c = [ni() for _ in range(n)]
mod = 10**9+7

c = rem_alone(compress(c))

prev = find_prev_idx(c)

dp = [0]*(len(c)+1)
dp[0] = 1
for i in range(1, len(c)+1):
    dp[i] = dp[i-1] if prev[i] == -1 else dp[i-1] + dp[prev[i]]
    dp[i] %= mod

    
print(dp[len(c)])