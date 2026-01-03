def gcd(a: int, b: int) -> int:
    """a, bの最大公約数(greatest common divisor: GCD)を求める
    計算量: O(log(min(a, b)))
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """a, bの最小公倍数(least common multiple: LCM)を求める
    計算量: O(log(min(a, b)))
    """
    return (a * b) // gcd(a, b)


def multi_gcd(array: list) -> int:
    """arrayのGCDを求める"""
    n = len(array)
    ans = array[0]
    for i in range(1, n):
        ans = gcd(ans, array[i])
    return ans


n, k = map(int, input().split())
a = list(map(int, input().split()))

gcd_ = multi_gcd(a)
if k % gcd_ == 0 and k <= max(a):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")