def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a
def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod
def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod



N = int(input())
K = int(input())
SN = str(N)
LN = list(SN)
keta =len(LN)
Nzer = keta-K
Nsei = K
output = 0
if keta>=K:
    output += comb(keta,K,10**9+7)*9**K
    t = 0
    s = 0
    while (s<=K-1)and(t<=keta-1):
        if LN[t]!="0":
            output -= (9-int(LN[t]))*comb(keta-1-t,K-1-s,10**9+7)*9**(K-1-s)
            t += 1
            s += 1
        elif LN[t]=="0":
            output -= (9-int(LN[t]))*comb(keta-1-t,K-1-s,10**9+7)*9**(K-1-s)
            t+=1
print(int(output))