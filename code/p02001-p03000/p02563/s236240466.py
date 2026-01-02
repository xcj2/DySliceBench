import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


# 998244353 = 119*2**23

mod = 998244353
primitive_root = 3  # mod の原始根
roots = [pow(primitive_root,(mod-1) >> i,mod) for i in range(24)]
inv_roots = [pow(r,mod-2,mod) for r in roots]
# roots[i] = 1 の 2**i 乗根、inv_roots[i] = 1 の 2**i 乗根の逆元


# 順番は変わる

def ntt(A,n):
    for i in range(n):
        m = 1 << (n-i-1)
        for start in range(1 << i):
            w = 1
            start *= m*2
            for j in range(m):
                A[start+j],A[start+j+m] = (A[start+j]+A[start+j+m]) % mod,(A[start+j]-A[start+j+m])*w % mod
                w *= roots[n-i]
                w %= mod
    return A


def inv_ntt(A,n):
    for i in range(n):
        m = 1 << i
        for start in range(1 << (n-i-1)):
            w = 1
            start *= m*2
            for j in range(m):
                A[start+j],A[start+j+m] = (A[start+j]+A[start+j+m]*w) % mod,(A[start+j]-A[start+j+m]*w) % mod
                w *= inv_roots[i+1]
                w %= mod
    a = pow(2,n*(mod-2),mod)
    for i in range(1 << n):
        A[i] *= a
        A[i] %= mod
    return A


def convolution(A,B):
    a,b = len(A),len(B)
    deg = a+b-2
    n = deg.bit_length()
    N = 1 << n
    A += [0]*(N-a)  # A の次数を 2冪-1 にする
    B += [0]*(N-b)  # B の次数を 2冪-1 にする
    A = ntt(A,n)
    B = ntt(B,n)
    C = [(A[i]*B[i]) % mod for i in range(N)]
    C = inv_ntt(C,n)
    return C[:deg+1]


N,M = MI()
A,B = LI(),LI()
print(*convolution(A,B))
