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

from bisect import bisect_right

a,b,q = li()
s = [ni() for _ in range(a)]
t = [ni() for _ in range(b)]
query = [ni() for _ in range(q)]

for qi in query:
    shrine_right = float('inf')
    temple_right = float('inf')
    
    shrine_right_idx = bisect_right(s, qi)
    temple_right_idx = bisect_right(t, qi)
    
    if shrine_right_idx < a:
        shrine_right = s[shrine_right_idx]
        
    if temple_right_idx < b:
        temple_right = t[temple_right_idx]
    
    shrine_left = float('inf')
    temple_left = float('inf')
    
    if shrine_right_idx > 0:
        shrine_left = s[shrine_right_idx - 1]
        
    if temple_right_idx > 0:
        temple_left = t[temple_right_idx - 1] 
        
    cand = []
    
    # 前前
    cand.append(max(abs(qi - shrine_left), abs(qi - temple_left)))
    
    # 前後
    cand.append(abs(temple_right-shrine_left) + min(abs(qi - shrine_left), abs(qi - temple_right)))
    
    # 後前
    cand.append(abs(shrine_right-temple_left) + min(abs(qi - temple_left), abs(qi - shrine_right)))
    
    # 後後
    cand.append(max(abs(qi - shrine_right), abs(qi - temple_right)))
        
    print(min(cand))