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

def n_based(n:int, base:int) -> str:
    if n == 0:
        return "0"
    
    ans = ""
    res = n
    
    while abs(res) > 0:
        q = res%base
        if q>=0:
            ans = str(q) + ans
            res //= base
        else:
            q += abs(base)
            ans = str(q) + ans
            res //= base
            res += 1
        
    return ans

n = ni()
print(n_based(n,-2))