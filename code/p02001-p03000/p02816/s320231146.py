import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
a = LI()
b = LI()

if N == 1:
    print(0,a[0]^b[0])
    exit()

A = [a[i] ^ a[i+1] for i in range(N-1)]
A = A + [a[N-1] ^ a[0]] + A
B = [b[i] ^ b[i+1] for i in range(N-1)]

# Aの長さN-1の連続部分列の中で、Bと一致するものは存在するか
# Rolling Hash


def f(mod,base):
    x = pow(base,N-1,mod)  # x = base**(N-1)

    d = 0  # Bのhash値
    for i in range(N-1):
        d *= base
        d += B[i]
        d %= mod

    c = 0  # Aの左N-1文字のhash値
    for i in range(N-1):
        c *= base
        c += A[i]
        c %= mod

    for i in range(N):
        if c == d:
            print(i,a[i] ^ b[0])
        c *= base
        c -= A[i]*x
        c += A[i+N-1]
        c %= mod


f(10**9+7,1234)
