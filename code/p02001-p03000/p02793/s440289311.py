def gcd(a: int, b: int) -> int:
    """a, bの最大公約数(greatest common divisor:GCD)を求める
    計算量: O(log(min(a, b)))
    """
    if b == 0:
        return a
    return gcd(b, a%b)


def lcm(a, b):
    """a, bの最小公倍数(least common multiple:LCM)を求める
    計算量: O(log(min(a, b)))"""
    return (a * b) // gcd(a, b)


def multi_gcd(array: list) -> int:
    """arrayのGCDを求める
    計算量: O(Nlog)
    """
    n = len(array)
    ans = array[0]
    for i in range(1, n):
        ans = gcd(ans, array[i])
    return ans


def multi_lcm(array):
    """arrayのLCMを求める"""
    ans = array[0]
    for i in range(1, len(array)):
        ans = (ans * array[i]) // gcd(ans, array[i])
    return ans


n = int(input())
MOD = 10**9 + 7
a = list(map(int, input().split()))
lcm_ = multi_lcm(a) % MOD
ans = 0
for i in range(n):
    ans += lcm_ * pow(a[i], MOD - 2, MOD)
    ans %= MOD
print(ans % MOD)
