import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
 
class Combination():
    # コンストラクタ
    def __init__(self, N:int, P:int):
        self.N = N
        self.P = P
 
        # fact[i] = (i! mod P)
        self.fact = [1, 1]   
        # factinv[i] = ((i!)^(-1) mod P)
        self.factinv = [1, 1]
        # factinv 計算用
        self.inv = [0, 1]    
 
        for i in range(2, N+1):
            self.fact.append((self.fact[-1] * i) % P)
            self.inv.append((-self.inv[P % i] * (P // i)) % P)
            self.factinv.append((self.factinv[-1] * self.inv[-1]) % P)
    
    # nCk (mod P)   (ただし、n<=N)
    def getComb(self, n:int, k:int):
        if (k < 0) or (n < k):
            return 0
        k = min(k, n - k)
        return self.fact[n] * self.factinv[k] * self.factinv[n-k] % self.P
 
def main():
    N,K = map(int,input().split())
    A = sorted([int(i) for i in input().split()])
 
    mod = 10**9+7
 
    COMB = Combination(N,mod)
 
    cmb = [0] * (N-K+1)
    for i in range(N-K+1):
        cmb[i] = COMB.getComb(i+(K-1),K-1)
 
    sum_max = 0
    for i in range(K-1,N):
        sum_max = (sum_max + cmb[i-(K-1)] * A[i]) % mod
 
    sum_min = 0
    for i in range(N-K,-1,-1):
        sum_min = (sum_min + cmb[(N-K)-i] * A[i]) % mod
 
    answer = sum_max - sum_min
    print(answer % mod)
 
if __name__ == "__main__":
    main()