import sys
input = sys.stdin.buffer.readline

def gcd(a: int, b: int) -> int:
    """a, bの最大公約数(greatest common divisor: GCD)を求める
    計算量: O(log(min(a, b)))
    """
    while b:
        a, b = b, a % b
    return a


def multi_gcd(array: list) -> int:
    """arrayのGCDを求める"""
    n = len(array)
    ans = array[0]
    for i in range(1, n):
        ans = gcd(ans, array[i])
    return ans


def make_mindiv_table(n):
    mindiv = [i for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if mindiv[i] != i:
            continue
        for j in range(2 * i, n + 1, i):
            mindiv[j] = min(mindiv[j], i)
    return mindiv


def get_prime_factors(num):
    res = []
    while mindiv[num] != 1:
        res.append(mindiv[num])
        num //= mindiv[num]
    return res


n = int(input())
a = list(map(int, input().split()))


mindiv = make_mindiv_table(10 ** 6)

set_primes = set()
flag = True
for val in a:
    set_ = set(get_prime_factors(val))
    for v in set_:
        if v in set_primes:
            flag = False
        set_primes.add(v)
    if not flag:
        break
else:
    print("pairwise coprime")
    exit()

gcd_ = multi_gcd(a)
if gcd_ == 1:
    print("setwise coprime")
    exit()

print("not coprime")