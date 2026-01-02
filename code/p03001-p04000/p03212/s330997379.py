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

stf = ["7","5","3"]
n = ni()

ans = 0
for pw in range(3,11):
    for i in range(3**pw):
        s = str(n_based(i,3)).zfill(pw)
        num = ""
        for i in range(pw):
            num += stf[int(s[i])]
            
        if int(num) <= n and ("3" in num and "5" in num and "7" in num):
            ans += 1
            
print(ans)