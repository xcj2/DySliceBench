import sys
input = sys.stdin.readline
X=int(input().rstrip())
maxX=10**6

def resolve():
    check,table=sieve(maxX)

    for a in table:
        if a>=X:
            print(a)
            return

def sieve(n):#n以下の素数を返す, is_prime[i]:iが素数ならtrue、table[i]:小さい順に素数入る
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    is_prime=[False]+is_prime ##[False]は勝手につけた、累積和をするときはこの影響で[0]+いらない
    return is_prime, table


import sys
from io import StringIO
import unittest

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
        input = """20"""
        output = """23"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """99992"""
        output = """100003"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()