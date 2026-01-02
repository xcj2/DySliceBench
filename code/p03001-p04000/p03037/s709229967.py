import sys
from itertools import accumulate
#booltable=[0]+booltable


def resolve():
    input = sys.stdin.readline
    N,M=map(int, input().rstrip().split())
    G=[list(map(int,input().rstrip().split())) for _ in range(M)]
    l=[0 for _ in range(N)]
    for i in range(M):
        l[G[i][0]-1]+=1
        if G[i][1]!=N:
            l[G[i][1]]-=1
    l=[0]+l
    cumsum=list(accumulate(l))#0~N

    ans=cumsum.count(int(M))
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
        input = """4 2
1 3
2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10 3
3 6
5 7
6 9"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """100000 1
1 100000"""
        output = """100000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()