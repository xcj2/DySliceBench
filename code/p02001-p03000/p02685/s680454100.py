import sys,os
from collections import defaultdict, deque
from math import ceil, floor, inf
if sys.version_info[1] >= 5:
    from math import gcd
else:
    from fractions import gcd
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
class Combinations:
    def __init__(self,n,p):
        self.n = n
        self.p = p
        self.g1 = [1,1]
        self.g2 = [1,1]
        inverse = [0,1]
        for i in range(2, self.n + 1):
            self.g1.append( ( self.g1[-1] * i ) % self.p )
            inverse.append( ( -inverse[self.p % i] * (self.p//i) ) % self.p )
            self.g2.append( (self.g2[-1] * inverse[-1]) % self.p )
    def nCr(self,r):
        if r < 0 or self.n < r:
            return 0
        r = min(r, self.n-r)
        return self.g1[self.n] * self.g2[r] * self.g2[self.n-r] % self.p

def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    MOD =  998244353

    N,M,K = LMIIS()
    ans = 0
    cmb = Combinations(N-1,MOD)
    #i個のブロックを連結、全体でN-i個、どこを連結させるかは(N-1)Ci通り
    for i in range(K,-1,-1):
        ans += M * pow(M-1,N-i-1,MOD) * cmb.nCr(i)
        ans %= MOD
    print(ans)

    

if __name__ == '__main__':
    main()