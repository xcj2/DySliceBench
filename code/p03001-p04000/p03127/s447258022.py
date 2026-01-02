n = int(input())
a = list(map(int, input().split()))

def gcd(a: int, b: int) -> int:
    """a, bの最大公約数(greatest common divisor: GCD)を求める
    計算量: O(log(min(a, b)))
    """
    if b == 0:
        return a
    return gcd(b, a%b)


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


print(multi_gcd(a))