import sys
from io import StringIO
import unittest
import heapq
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
        input = """3 3
2 13 8"""
        output = """9"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 4
1 9 3 5"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1 100000
1000000000"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """9500000000"""
        self.assertIO(input, output)
def resolve():
    (n,m)=(int(i) for i in input().split())
    A=[int(i) for i in input().split()]
    q=[]
    for i in A:
        heapq.heappush(q,-i)
    for i in range(m):
        x=q[0]
        heapq.heappushpop(q,int(x/2))
    print(-sum(q))
if __name__ == "__main__":
    resolve()