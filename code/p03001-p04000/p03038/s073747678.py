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
        input = """3 2
5 1 4
2 3
1 5"""
        output = """14"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10 3
1 8 5 7 100 4 52 33 13 5
3 10
4 30
1 4"""
        output = """338"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3 2
100 100 100
3 99
3 99"""
        output = """300"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """11 3
1 1 1 1 1 1 1 1 1 1 1
3 1000000000
4 1000000000
3 1000000000"""
        output = """10000000001"""
        self.assertIO(input, output)

def resolve():
    (N,M)=(int(i) for i in input().split())
    A=[int(i) for i in input().split()]
    A.sort()
    BC=[[int(i) for i in input().split()] for i in range(M)]
    BC.sort(key=lambda x: x[1] , reverse=True)
    fst=0
    for i in BC:
        cnt=i[0]
        val=i[1]
        while  cnt>0:
            if fst>=N:
                break
            if A[fst]<val:
                A[fst]=val
                cnt-=1
                fst+=1
            else:
                break
        else:
            continue
        break
    print(sum(A))



if __name__ == "__main__":
    resolve()