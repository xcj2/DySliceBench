import sys
from itertools import accumulate

def resolve():
        input = sys.stdin.readline
        N=int(input().rstrip())
        #S=input()
        #a=len(S)
        S=list(input().rstrip().replace("W","1").replace("E","0"))

        csum=["0"]+S
        csum=list(map(int,csum))
        csum=list(accumulate(csum))#Wの数
        ans=N
        for i in range(1,N+1,1):
            numWleft=csum[i-1]-csum[0]
            numEright=(N-i)-(csum[N]-csum[i])
            ans=min(ans,numWleft+numEright)
        print(ans)

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
WEEWW"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """12
WEWEWEEEWWWE"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8
WWWWWEEE"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()