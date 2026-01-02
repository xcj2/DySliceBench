import sys
from io import StringIO
import unittest
from itertools import accumulate
def resolve():
    end=100000
    input=sys.stdin.readline
    N,C=map(int,input().rstrip().split())
    S=[list(map(int,input().rstrip().split())) for _ in range(N)]

    l=[[0 for _ in range(C)] for __ in range(2*end)]
    for i in range(N):
        l[S[i][0]*2-1][S[i][2]-1]+=1
        if S[i][1]!=end:
            l[S[i][1]*2+1][S[i][2]-1]-=1
    """
    ans=0
    npl=np.array(l)
    for i in range(C):
        snpl=npl[:,i]
        buf=list(snpl)
        asum = list(accumulate(buf))
        M=max(asum)
        ans=max(ans,M)
    """
    asum=[0 for __ in range(2*end)]
    for i in range(2*end):#列(C)で和を取る
        for j in range(C):
            asum[i]+=l[i][j]
    asum2=list(accumulate(asum))
    ans=max(asum2)
    ans=min(ans,C)

    print(int(ans))

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
1 7 2
7 8 1
8 12 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 4
1 3 2
3 4 4
1 4 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """9 4
56 60 4
33 37 2
89 90 3
32 43 1
67 68 3
49 51 3
31 32 3
70 71 1
11 12 3"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()