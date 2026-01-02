import sys
from io import StringIO
import unittest
import math

def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]


def resolve():
    q = int(input())
    lr = [list(map(int, input().split())) for _ in range(q)]

    # 素数のlist
    prime_list = set(primes(10 ** 5 + 1)) # setにしないと、ものすごい遅い

    """
    # 10^5 * 10 ^ 5なので✗
    for l, r in lr:
        tmp = 0
        for i in range(l, r + 1):
            if i in prime_list and (i + 1)/2 in prime_list:
                tmp += 1
        print(tmp)
    """

    cum_2017 = [0, 0]
    # 累積和的に、2017に似た数カウントをする
    tmp = 0
    for i in range(2, 10 ** 5 + 1, 1):
        if i in prime_list and (i + 1) / 2 in prime_list: # (i + 1) // 2 でなく、(i + 1) / 2にすると遅い
            tmp += 1
            cum_2017.append(tmp)
        else:
            cum_2017.append(tmp)

    for l, r in lr:
        print(cum_2017[r] - cum_2017[l - 1])



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """1
3 7"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
13 13
7 11
7 11
2017 2017"""
        output = """1
0
0
1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6
1 53
13 91
37 55
19 51
73 91
13 49"""
        output = """4
4
1
1
1
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()