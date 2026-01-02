def factorial_mod(a, M):
    # return a!(mod M)
    ans = 1
    for i in range(a,1,-1):
        ans = (ans * i) % M
    return ans
def test(n, a, M):
    # return (nCaの分子) % M
    ans = 1
    for i in range(a):
        ans = (ans * (n-i)) % M
    return ans
def combination_mod(n,a,M):
    # return nCa % M
    tmp = factorial_mod(a,M)
    tmp = pow(tmp, M-2, M)
    ans = test(n,a,M) * tmp % M
    return ans
def output(n,a,b):
    M = 10**9+7
    ans = (pow(2,n,M) - 1 - combination_mod(n,a,M) - combination_mod(n,b,M)) % M
    return ans
n, a, b = map(int, input().split())
print(output(n,a,b))