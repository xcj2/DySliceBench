import sys 
from itertools import accumulate
input=sys.stdin.readline
Q=int(input().rstrip())
S=[list(map(int,input().rstrip().split())) for _ in range(Q)]


def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    is_prime=[False]+is_prime
    return is_prime, table


def resolve():
    maxN=10**5+1
    booltable1,table1=sieve(maxN)
    booltable2,table2=sieve((maxN+1)//2)
    booltable=[0 for _ in range(maxN+1)]
    for i in range(1,maxN+1,2):
        booltable[i]=booltable1[i] and booltable2[(i+1)//2]
    # 累積和
    #booltable=[0]+booltable
    cumsum = list(accumulate(booltable))

    for i in range(Q):
        print(cumsum[S[i][1]]-cumsum[S[i][0]-1])
    
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
    #unittest.main()
    resolve()