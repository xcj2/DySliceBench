def mod_kaijou(n,MOD = 10 ** 9 + 7 ):
    ans = 1
    for i in range(1,n + 1):
        ans *= i
        ans %= MOD
    return ans
# def pow_r(x, n,MOD = 1):
#     """
#     O(log n)
#     """
#     if n == 0:  # exit case
#         return 1
#     if n % 2 == 0:  # standard case ① n is even
#         return pow_r(x ** 2, n // 2) % MOD
#     else:  # standard case ② n is odd
#         return x * pow_r(x ** 2, (n - 1) // 2) % MOD

def 逆元_一覧(n,MOD = 10 ** 9 + 7):
    li = [0]
    for i in range(1,n+ 1):
        li.append(pow(i,MOD-2,MOD))
    return li


def mod_nCr(n,r,MOD = 10 ** 9 + 7 ):
    ans = 1
    mul = n
    li = 逆元_一覧(r + 1)
    for i in range(r ):
        ans *= mul
        ans *= li[i + 1]
        mul -= 1
        ans %= MOD
    return ans


MOD= 10 ** 9 + 7
n,a,b = list(map(int,input().split()))
all = pow(2,n,MOD)  - 1
all %= MOD
A = mod_nCr(n,a,MOD)
all -= A
all %= MOD
B = mod_nCr(n,b,MOD)
all -= B
all %= MOD
print(all)