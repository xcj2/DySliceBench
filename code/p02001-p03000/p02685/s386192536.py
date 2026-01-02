def comb(n,r,m):
    if r == 0: return 1
    return memf[n]*pow(memf[r],m-2,m)*pow(memf[n-r],m-2,m)
def mempow(a,b):
    temp = 1
    yield temp
    for i in range(b):
        temp = temp * a % 998244353
        yield temp
def memfact(a):
    temp = 1
    yield temp
    for i in range(1,a+1):
        temp = temp * i % 998244353
        yield temp

N,M,K = (int(x) for x in input().split())
memp = []
memf = []
mpappend = memp.append
mfappend = memf.append
for x in mempow(M-1,N-1):
    mpappend(x)
for x in memfact(N-1):
    mfappend(x)
ans = 0
if M == 1:
    if K + 1 < N:
        print('0')
    else:
        print('1')
else:
    i = 0
    for i in range(K+1):
        ans = (ans + (comb(N-1,i,998244353)*M*memp[N-i-1])) % 998244353
    print(ans)