import sys

def resolve():
        input = sys.stdin.readline
        N=int(input().rstrip())

        A=[[0] * 3 for i in range(N)]
        for i in range(N):
            A[i][:]=list(map(int,input().rstrip().split()))

        dp=[[0] * 3 for i in range(N)]
        for j in range(3):
            dp[0]=A[0]

        for i in range(1,N,1):
            for j in range(3):
                for k in range(3):
                    if(k!=j):
                        dp[i][j]=max(dp[i][j],dp[i-1][k]+A[i][j])
       
        print(max(dp[N-1]))
          
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
10 40 70
20 50 80
30 60 90"""
        output = """210"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1
100 10 1"""
        output = """100"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1"""
        output = """46"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()