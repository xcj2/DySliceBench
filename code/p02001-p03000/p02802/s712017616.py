import sys

def resolve():
    input = sys.stdin.readline
    N,M=map(int,input().rstrip().split())
    Q=[list(input().rstrip().split()) for _ in range(M)]

    c=[0 for _ in range(N)]
    flag=[0 for _ in range(N)]

    for i in range(M):
        if Q[i][1]=="WA" and flag[int(Q[i][0])-1]==0:
            c[int(Q[i][0])-1]+=1
        if Q[i][1]=="AC":
            flag[int(Q[i][0])-1]=1
    
    #ans=sum(c)
    #ansAC=sum(flag)
    
    ans=0
    ansAC=0
    for i in range(N):
        if flag[i]==1:
           ans+=c[i]
        ansAC+=flag[i]
    #print(int(ansAC), int(ans))
    print('{:.15g}'.format(ansAC),'{:.15g}'.format(ans))


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
        input = """2 5
1 WA
1 AC
2 WA
2 AC
2 WA"""
        output = """2 2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """100000 3
7777 AC
7777 AC
7777 AC"""
        output = """1 0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 0"""
        output = """0 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()