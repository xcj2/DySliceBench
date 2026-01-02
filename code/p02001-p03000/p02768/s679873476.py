mod = 10**9+7
n,a,b = [int(i) for i in input().split()]
k = min(n,2*(10**5))
import sys
sys.setrecursionlimit(100000000)
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
ans = pow_k(2,n,mod)
cmb = combination_list(n,mod)
ans -=1
ans -= cmb[a]
if ans < 0:
    ans += mod
ans -= cmb[b]
if ans <0:
    ans += mod
print(ans)