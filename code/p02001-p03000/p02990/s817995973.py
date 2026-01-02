import sys
sys.setrecursionlimit(10**5)
def solve():
    N, K = map(int,input().split())
    MOD = 10 ** 9 + 7
    ans = []
    for i in range(1,K+1):
        com1 = COM(K-1,i-1,MOD)
        if N-K-(i-1) < 0:
            ans.append(0)
            continue
        com2 = COM(N-K+1,N-K-(i-1),MOD)
        ans.append(com1*com2%MOD)
    
    print(*ans,sep='\n')

def COM(n,r,MOD):
    return calcNumerator(n,r,MOD) // calcDenominator(r,MOD)

def calcNumerator(n,r,MOD):
    res = 1
    for i in range(r):
        res *= n % MOD
        n -= 1
    return res

def calcDenominator(r,MOD):
    res = 1
    a = r
    for i in range(r):
        res *= a % MOD
        a -= 1
    return res

if __name__ == '__main__':
    solve()