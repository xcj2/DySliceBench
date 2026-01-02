

n, a, b = map(int, input().split())

# 階乗
def fact(n, mod):
    ans = 1
    for i in range(1, n+1):
        ans = (ans*i) % mod
    return ans

# 繰り返し２乗法
def pow(a, n, mod):
    if n == 0:
        return 1
    if n%2 == 0:
        t = pow(a, n//2, mod)
        return t*t % mod
    return a * pow(a, n-1, mod)


# 組み合わせ
def comb(n, a, mod):
    val = pow(fact(a, mod), mod-2, mod)

    p = 1
    for i in range(a):
        p = (p*(n-i)) % mod
    return val*p %mod


mod = 10**9+7
allptn = pow(2, n, mod)
aptn = comb(n, a, mod)
bptn = comb(n, b, mod)

ans = (allptn-1 - aptn - bptn) % mod
print(ans)