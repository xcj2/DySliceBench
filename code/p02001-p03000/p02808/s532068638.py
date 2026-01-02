import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N,K,*A = map(int,read().split())

MOD = 10 ** 9 + 7

def cumprod(A, MOD = MOD):
    L = len(A); Lsq = int(L**.5+1)
    A = np.resize(A, Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        A[:,n] *= A[:,n-1]; A[:,n] %= MOD
    for n in range(1,Lsq):
        A[n] *= A[n-1,-1]; A[n] %= MOD
    return A.ravel()[:L]
def make_fact(U, MOD = MOD):
    x = np.arange(U, dtype = np.int64); x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64); x[0] = pow(int(fact[-1]), MOD-2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact,fact_inv

def convolve(f, g, MOD=MOD):
    """
    数列 (多項式) f, g の畳み込みの計算．上下 15 bitずつ分けて計算することで，
    30 bit以下の整数，長さ 250000 程度の数列での計算が正確に行える．
    """
    Lf = len(f); Lg = len(g); L = Lf + Lg - 1
    fl = f & (1 << 15) - 1; fh = f >> 15
    gl = g & (1 << 15) - 1; gh = g >> 15
    if L < (1<<8):
        conv = lambda f,g: \
            np.convolve(f,g) % MOD
    else:
        fft = np.fft.rfft; ifft = np.fft.irfft; fft_len = 1 << L.bit_length()
        conv = lambda f,g: \
            np.rint(ifft(fft(f,fft_len) * fft(g,fft_len))[:L]).astype(np.int64) % MOD
    x = conv(fl, gl)
    z = conv(fh, gh)
    y = conv(fl+fh, gl+gh)
    return (x + ((y - x - z) << 15) + (z << 30)) % MOD

fact, fact_inv = make_fact(10 ** 5)

f = np.zeros(N+1,np.int64)
f[0] = 1
for a in A:
    g = fact[N-a:N+1] * fact_inv[0:a+1] % MOD * fact_inv[N-a] % MOD
    g = g[::-1]
    g *= fact_inv[:len(g)]; g %= MOD
    f = convolve(f,g)[:N+1]

f *= fact[:N+1]; f %= MOD

answer = f[N]
print(answer)
