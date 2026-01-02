import sys
sys.setrecursionlimit(1 << 25)
readline = sys.stdin.buffer.readline
read = sys.stdin.readline  # 文字列読み込む時はこっち
ra = range
enu = enumerate


def exit(*argv, **kwarg):
    print(*argv, **kwarg)
    sys.exit()


def mina(*argv, sub=1): return list(map(lambda x: x - sub, argv))
# 受け渡されたすべての要素からsubだけ引く.リストを*をつけて展開しておくこと


def a_int(): return int(readline())


def ints(): return list(map(int, readline().split()))


def _make_prime_numbers(N: int):
    # N以下の素数を列挙 -> set
    # まずエラトステネスの篩を作成
    is_prime = [True] * (N + 1)
    is_prime[0] = False  # 0と1は素数ではない
    is_prime[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, N + 1, i):  # iの倍数は素数でない
                is_prime[j] = False

    primes = []
    for i, flg in enumerate(is_prime):
        if flg:
            primes.append(i)

    return primes


primes = _make_prime_numbers(10**6)


from bisect import bisect_left


def fast_factorization(N: int):
    # -> List[Tuple[int,int]] (素数,冪数)を格納
    # 素数配列primesを使ってO(log N)で因数分解
    if N == 1:
        return []  # 1は素数ではない
    # 素因数分解
    arr = []
    temp = N
    for p in primes[:bisect_left(primes, N**(1 / 2)) + 1]:
        if temp % p == 0:
            cnt = 0
            while temp % p == 0:
                cnt += 1
                temp //= p
            arr.append((p, cnt))
            if temp == 1:  # 早期終了
                break

    if temp != 1:  # √Nより大きい素因数はたかだか1個ある
        arr.append((temp, 1))
    if arr == []:  # 自身が素数だった場合
        arr.append((temp, 1))

    return arr


MOD = 10**9 + 7
INF = 2**31  # 2147483648 > 10**9
# default import
from collections import defaultdict, Counter, deque
from math import gcd


N = a_int()
A = ints()

# setかはすぐわかる
# setでなければ not coprime
# pairは互いに素かをみればいいのか
# つまり因数分解して足してったときにすべての素数のべき数が1以下であれば良い

g_set = 0
cnt = defaultdict(lambda: 0)
flg = 1  # pairwiseであるフラグ
for a in A:
    g_set = gcd(g_set, a)
    if flg:
        for p, n in fast_factorization(a):
            if cnt[p] != 0:
                flg = 0
            cnt[p] += n


# print(cnt)
# for v in cnt.values():
#     if v > 1:
#         flg = 0
#         break

if g_set > 1:
    print('not coprime')
elif flg:
    print('pairwise coprime')
else:
    print('setwise coprime')
