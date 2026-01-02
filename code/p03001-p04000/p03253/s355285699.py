inf = 10**15
mod = 10**9+7


# nCr

def ruijo(n, l, mod):
    a = n
    tmp = n - 1
    while (tmp >= l):
        a = a * tmp % mod
        tmp -= 1
    return a


def cmb(n, r, mod):
    if r == 1:
        return n
    elif (n == r or r == 0):
        return 1
    else:
        if (r < 0 or r > n):
            return 0
        r = min(r, n - r)
        return ruijo(n, n - r + 1, mod) * g2[r] % mod


mod = 10 ** 9 + 7  # 出力の制限
N = 10 ** 6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
def factorization(n):
    arr = []
    temp = n
    if n == 1:
        return arr

    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

n,m = map(int, input().split())
if m == 1:
    print(1)
else:
    bpre = factorization(m)
    ans = 1
    for tmp in bpre:
        b = tmp[1]
        ans *= cmb(n-1+b, n-1, mod)
        ans = ans%mod
    print(ans)