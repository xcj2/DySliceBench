import sys
from itertools import accumulate

def resolve():
        input = sys.stdin.readline
        N=int(input().rstrip())
        A1=list(map(int,input().rstrip().split()))
        A2=list(map(int,input().rstrip().split()))

        csumA1=[0]+A1
        csumA2=[0]+A2
        csumA1=list(accumulate(csumA1))
        csumA2=list(accumulate(csumA2))
        sum=0
        for i in range(1,N+1,1):
            sumA1=csumA1[i]-csumA1[0]
            sumA2=csumA2[N]-csumA2[i-1]
            sum=max(sum,sumA1+sumA2)
        print(sum)



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
        input = """5
3 2 2 4 1
1 2 2 2 1"""
        output = """14"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
1 1 1 1
1 1 1 1"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """7
3 3 4 5 4 5 3
5 3 4 4 2 3 2"""
        output = """29"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1
2
3"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()