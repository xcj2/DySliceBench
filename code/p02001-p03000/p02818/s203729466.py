import sys
input = sys.stdin.readline
A,B,K=map(int,input().rstrip().split())

def resolve():
    
    if(A>K):
        ansA=int(A)-int(K)
        ansB=int(B)
    else:
        ansA=0
        ansB=int(B)-(int(K)-int(A))
        if(ansB<0):
            ansB=0
    print(str(int(ansA))+" "+str(int(ansB)))

import sys
from io import StringIO
import unittest
#1000000000000 1000000000000 1000000000001
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
        input = """2 3 3"""
        output = """0 2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """500000000000 500000000000 1000000000000"""
        output = """0 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()