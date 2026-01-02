#template
def inputlist(): return [int(j) for j in input().split()]
#template

def pow_k(a,n,mod):
    if n == 0:
        return 1
    if n % 2 ==0:
        return pow_k(a*a % mod,n//2,mod)
    else:
        return a * pow_k(a,n-1,mod) % mod
def modinv(a, mod):
    return pow(a, mod-2, mod)
def combination_list(n, mod):
    lst = [1]
    for i in range(1, k+1):
        lst.append(lst[-1] * (n+1-i) % mod * modinv(i, mod) % mod)
    return lst
def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res
def chofuku_cmb(n, r, mod=10**9+7):
    return combination(n+r-1, r, mod)

S = int(input())
mod = 10**9+7
if S < 3:
    print(0)
    exit()
N = S // 3
d = S % 3
ans = 0
for i in range(N):
    if i != 0:
        d += 3
    tmp = chofuku_cmb(N-i,d,mod)
    ans += tmp
    ans %= mod
ans %= mod
print(ans)