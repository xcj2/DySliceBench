import cmath
pi = cmath.pi
exp = cmath.exp

import sys
readline = sys.stdin.readline
write = sys.stdout.write

def make_exp_t(N, base):
    exp_t = {0: 1}
    temp = N
    while temp:
        exp_t[temp] = exp(base / temp)
        temp >>= 1
    return exp_t

def fft_dfs(f, s, N, st, exp_t):
    if N==2:
        a = f[s]; b = f[s+st]
        return [a+b, a-b]
    N2 = N//2; st2 = st*2
    F0 = fft_dfs(f, s   , N2, st2, exp_t)
    F1 = fft_dfs(f, s+st, N2, st2, exp_t)
    w = exp_t[N]; wk = 1.0
    for k in range(N2):
        U = F0[k]; V = wk * F1[k]
        F0[k] = U + V
        F1[k] = U - V
        wk *= w
    F0.extend(F1)
    return F0

def fft(f, N):
    if N==1:
        return f
    return fft_dfs(f, 0, N, 1, fft_exp_t)

def ifft(F, N):
    if N==1:
        return F
    f = fft_dfs(F, 0, N, 1, ifft_exp_t)
    for i in range(N):
        f[i] /= N
    return f

N,M = map(int,input().split())

l = 10**5+1
L = 2**(2*l-1).bit_length()

power = list(map(int,input().split()))
count = [0.0 for _ in range(l)]

for p in power:
    count[p] += 1

fft_exp_t = make_exp_t(L, -2j*pi)
ifft_exp_t = make_exp_t(L, 2j*pi)

count.extend([0]*(L-l))

C = fft(count, L)

CC =[C[i]*C[i] for i in range(L)]

cc = ifft(CC,L)

shake = 0
ans = 0

for i in reversed(range(len(cc))):
    if shake+int(cc[i].real+0.5)<=M:
        ans += i*int(cc[i].real+0.5)
        shake += int(cc[i].real+0.5)
    else:
        ans += i*(M-shake)
        break
        
print(ans)