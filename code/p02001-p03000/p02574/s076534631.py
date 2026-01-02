from math import gcd
from math import floor
from collections import defaultdict

def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def factorize(N):  # 素因数分解
    prime = set()
    for p in prime_list:
        if p * p > N:
            break
        while N % p == 0:
            N //= p
            prime.add(p)
    if N > 1:
        prime.add(N)
    return prime


n = int(input())
a = list(map(int, input().split()))

ans = 0
for ai in a:
    ans = gcd(ans, ai)
if ans != 1:
    print('not coprime')
    exit()

prime_list = eratosthenes(10 ** 6)
num = set()

class PrimeFactorization:
    '''1つの因数分解クエリをO(log(k))で実行する（初期化にO(N))
    >>> pf = PrimeFactorization(100)
    >>> pf.query(100)
    ((2, 2), (5, 2))
    
    '''
    # https://atcoder.jp/contests/abc177/editorial/82
    # 高速素因数分解
    # 問題： A 以下の数が N 個与えられる。全て素因数分解せよ。
    # 前計算としてエラトステネスの篩を行い、「その数をふるい落とした素数」を配列 D に記録します。
    # 例えば D[4]=D[6]=2,D[35]=5 です。x が素数のときは D[x]=x としておきます。この配列はエラトステネスの篩と同様 O(AloglogA) で構築できます。
    # D[x] は x を割り切る最小の素数なので、この配列 D を利用すると素因数分解を行うときに「試し割り」をする必要がなくなり(D[x]で割ればよい)、1つの数の素因数分解が素因数の個数である O(logA) でできるようになります。
    from collections import defaultdict
    def __init__(self, Num=10**6):
        self.Num = Num
        self.D = [-1] * (Num+1)
        for i in range(2, Num+1):
            if self.D[i] != -1:
                continue
            self.D[i] = i
            for j in range(1, floor(Num/i)+1):
                if self.D[j*i] != -1:
                    continue
                else:
                    self.D[j*i] = i
    
    def query(self, k):
        ans = defaultdict(int)
        tmp = k
        while self.D[tmp] != -1:
            div = self.D[tmp]
            ans[div] += 1
            tmp = tmp//div
        return set(ans.keys())
      
pf = PrimeFactorization(10**6)
for ai in a:
    prime = pf.query(ai)
    # prime = factorize(ai)
    if len(prime & num) > 0:
        print('setwise coprime')
        break
    num |= prime
else:
    print('pairwise coprime')
