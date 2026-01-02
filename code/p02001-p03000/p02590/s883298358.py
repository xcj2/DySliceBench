import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
A = LI()
B = []
for i in range(N):
    if A[i] != 0:
        B.append(A[i])
N = len(B)
P = 200003

# 2はPの原始根

C = []  # C[i] = (2**i mod P)
d = {}  # d[n] = (2**i == n たるi)
a = 1
for i in range(P-1):
    C.append(a)
    d[a] = i
    a *= 2
    a %= P

D = [0]*(P-1)
for i in range(N):
    D[d[B[i]]] += 1

n = 2**((2*P-3).bit_length())
D += [0]*(n-(P-1))


from cmath import pi,exp

def dfs(f,start,step,N,inverse=False):
    if N == 2:
        a,b = f[start],f[start+step]
        return [a+b,a-b]
    if inverse is False:
        f0 = dfs(f,start,2*step,N//2,inverse=False)
        f1 = dfs(f,start+step,2*step,N//2,inverse=False)
        z = exp(2j*pi/N)
    else:
        f0 = dfs(f,start,2*step,N//2,inverse=True)
        f1 = dfs(f,start+step,2*step,N//2,inverse=True)
        z = exp(-2j*pi/N)
    z0 = 1.0
    for i in range(N//2):
        a,b = f0[i],f1[i]*z0
        f0[i],f1[i] = a+b,a-b
        z0 *= z
    return f0+f1

def DFT(f,N):  # fを離散フーリエ変換
    if N == 1:
        return f
    return dfs(f,0,1,N)

def iDFT(F,N):  # Fを離散フーリエ逆変換
    if N == 1:
        return F
    f = dfs(F,0,1,N,inverse=True)
    for i in range(N):
        f[i] /= N
    return f

# deg(f)+deg(g)<Nとなる2冪Nを選び、f,gの長さがNになるように0を埋めておく

def product(f,g,N):  # 多項式f,gの積
    F = DFT(f,N)
    G = DFT(g,N)
    FG = [F[i]*G[i] for i in range(N)]
    fg = iDFT(FG,N)
    for i in range(N):
        fg[i] = int(fg[i].real+0.5)
    return fg


E = product(D,D,n)
ans = 0
for i in range(P-1):
    ans += (C[i]*(E[i]+E[i+(P-1)]))

for i in range(N):
    ans -= (B[i]**2) % P

print(ans//2)
