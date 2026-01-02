import sys
input = sys.stdin.readline

def matDot(A,B,MOD):
    N,M,L = len(A),len(A[0]),len(B[0])
    
    res = [[0]*L for i in range(N)]

    for i in range(N):
        for j in range(L):
            s = 0
            for k in range(M):
                s = (s + A[i][k]*B[k][j]) % MOD
            res[i][j] = s
    
    return res

def matPow(A,x,MOD):
    N = len(A)
    res = [[0]*N for i in range(N)]
    
    for i in range(N):
        res[i][i] = 1
    
    for i in range(x.bit_length()):
        if (x>>i) & 1:
            res = matDot(res,A,MOD)
        A = matDot(A,A,MOD)
    
    return res

def main():
    n,k = map(int,input().split())
    mod = 10**9+7

    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))

    b = matPow(a,k,mod)

    ans = 0
    for i in range(n):
        for j in range(n):
            ans = (ans+b[i][j])%mod

    print(ans)

if __name__ == "__main__":
    main()