from collections import Counter

def resolve():
    # 方針
    # LCMを求めたい
    #  Aを素因数分解して、素因数ごとに肩のmaxを取りに行く
    #  max同士を掛け合わせる
    # B = X / A : 逆元
    #  B = A^(p-2) , p: 素数 prime

    # たくさんの数の素因数分解
    #     (1こだけの場合。Xに対し、sqrt(X)まで順に見て割り切れなければ素数として判定)
    #  (1) 素数列挙
    #    エラトステネスの篩
    #     素数と決まった数の倍数を消していく(最初は2)
    #     次の数にいく。消されてなければ素数。その数の倍数を消していく。(2乗となる倍数から開始すれば良い)　-> O(NloglogN)
    #     
    #  (2) 素因数分解
    #     上記の操作の時、何で割られたかメモしていく。すでに書かれているものは上書きしない。
    #     例:36. 36 ->2-> 18 ->2-> 9 ->3-> 3(prime) = 2x2x3x3 (sorted)
    #    => 素因数分解の完了
    # 
    MOD = 10**9 + 7
    N = int(input())
    A = list(map(int, input().split()))

    # 素数列挙 & 割った数の計算
    MX = int(10**6)
    L = [0] * (MX + 1)
    L[0] = -1
    L[1] = -1
    primes = []

    for i in range(2, MX+1):
        if L[i]:
            continue
        primes.append(i)
        L[i] = i
        for j in range(i*i, MX+1, i):
            if L[j] == 0:
                L[j] = i

    def factor(x: int):
        res = []
        while x != 1:
            prime = L[x] if L[x] != 0 else x
            res.append(prime)
            x /= prime
            x = int(x)
        return res

    max_e = {}
    for a in A:
        a = Counter(factor(a))
        for key, v in a.items():
            if not key in max_e:
                max_e[key] = v
            else:
                if v > max_e[key]:
                    max_e[key] = v
    # print(max_e)

    def modinv(a, mod=10**9+7):
        return pow(a, mod-2, mod)

    lcm = 1
    for key, v in max_e.items():
        lcm *= key ** v

    # print(max_e)
    # print(lcm)
    lcm %= MOD
    # print(lcm)

    ans = 0
    for i in range(N):
        b = lcm * modinv(A[i]) 
        ans += b

    print(int(ans % MOD))


def resolve_ref():
    from fractions import gcd
    
    mod = 10 ** 9 + 7
    
    N = int(input())
    A = list(map(int, input().split()))
    
    L = 1
    for a in A:
        L *= a // gcd(L, a)
    
    print(L)
    L %= mod
    print(L)
    
    print(sum(L * pow(a, mod - 2, mod) for a in A) % mod)

if __name__ == "__main__":
    resolve()