import sys
from collections import deque


   
def resolve():
    
    input = sys.stdin.readline
    N,K=map(int,input().rstrip().split())
    R,S,P=map(int,input().rstrip().split())
    T=list(input().rstrip())

    ans=0
    flag=[0 for _ in range(N)]
    for i in range(N):
        if T[i]==T[i-K] and i>=K and flag[i-K]==True: #足さない条件、K個前が既に制約で足せなくなっていた時は、今回は足せるようになるのでflag管理
            continue
        if T[i]=="r":
            ans+=P
        if T[i]=="s":
            ans+=R
        if T[i]=="p":
            ans+=S
        flag[i]=True
    print(ans)

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
        input = """5 2
8 7 6
rsrpr"""
        output = """27"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7 1
100 10 1
ssssppr"""
        output = """211"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr"""
        output = """4996"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()