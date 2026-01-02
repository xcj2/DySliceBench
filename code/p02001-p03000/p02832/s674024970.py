from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007
"""
#N,K,Mが入力
    n,k,m=LI() 
    #N
    #x1 y1
    #.  .
    #xn ynが入力
    N=I()
    p=LIR(N)
    print(n,k,m,p)
"""
def resolve():
    n=I()
    a=LI()

    numc=1
    breakc=0
    
    for i in range(n):
        if a[i]==numc:
            numc+=1
        else:
            breakc+=1
    if numc==1:
        print(-1)
    else:
        print(breakc)

    return

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
        input = """3
2 1 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
2 2 2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """10
3 1 4 1 5 9 2 6 5 3"""
        output = """7"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1
1"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()