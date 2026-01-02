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

from itertools import accumulate

n,q = li()
a = list(li())
x = [ni() for _ in range(q)]


cum_nor = list(accumulate(a))
cum_odd = list(accumulate(a[::2]))
cum_evn = list(accumulate(a[1::2]))
cum_kog = [cum_odd[i//2] if i%2==0 else cum_evn[i//2] for i in range(n)]

# 高橋君が左からtak個取れるならTrue そうでないならFalse
def check(a:list, tak:int, pivot:int):
    if tak > (len(a)+1)//2:
        return False
    
    if pivot-a[-2*tak+1] > a[-tak]-pivot:
        return False
    else:
        return True
        
    
def binsearch(a:list,xi:int):
    low = 1
    high = len(a)
    while high-low > 1:
        mid = (high+low) // 2
        if check(a,mid,xi):
            low = mid
        else:
            high = mid
            
    return low


for xi in x:
    tak = binsearch(a,xi)
    ans = cum_nor[-1] - cum_nor[-tak-1]
    if 2*tak < n:
        ans += cum_kog[-2*tak-1] 
    
    print(ans)