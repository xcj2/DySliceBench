import sys
MOD = 10**9 + 7
def sinput(): return sys.stdin.readline().strip()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(n=0):
    if n: return [0 for _ in range(n)]
    else: return list(imap())
def farr(): return list(fmap())
def sarr(n=0):
    if n: return ["" for _ in range(n)]
    else: return sinput().split()
def barr(n): return [False for _ in range(n)]
def adj(n): return [[] for _ in range(n)]

def inv(a): return pow(a, MOD-2, MOD) #逆元
def comb(n,r):
    ans = 1
    for i in range(r): ans *= n-i; ans *= inv(r-i); ans %= MOD
    return ans

    
n,k = imap()
ans = n-k+1
print(ans)
for i in range(2,k+1):
    ans *= (n-k-i+2) * (k-i+1) * inv(i) * inv(i-1)
    print(ans %MOD)
