from functools import lru_cache
from collections import defaultdict
MOD = 10**9 + 7


def Is_prime(n):
    # nが1以下ならFalse
    if n<=1:
        return False
    # nが2または3ならTrue
    if n==2 or n==3:
        return True
    # nが2の倍数ならFalse
    if n%2==0:
        return False
    # nの平方根を整数で取得
    sqrt_root = int(n**.5)
    # nがnの平方根以下の3以上の奇数で1回でも割れたらFalse
    for i in range(3,sqrt_root+1,2):
        if n%i==0:
            return False
    # 上の条件を全てぬけたものはTrue
    return True

# 素数テーブル
# n以下の素数を列挙する
def Prime_table(n):
    res = []
    for i in range(n+1):
        if Is_prime(i):
            res.append(i)
    return res

# 素因数分解
def Factorization(n):
    prime_table = Prime_table(n)
    arr = []
    temp = n
    for i in prime_table:
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

N = int(input())
L = list(map(Factorization, range(2,N+1)))

d = defaultdict(int)
for i in range(len(L)):
    for l in L[i]:
        d[l[0]] += l[1]

res = 1
for i in d.values():
    res *= (i+1)
    res %= MOD
print(res)