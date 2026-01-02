import sys
from collections import deque

def resolve():
    input=sys.stdin.readline
    N,Q=map(int,input().rstrip().split())
    S=list(input().rstrip())
    R=[list(map(int,input().rstrip().split())) for _ in range(Q)]
    cumsum=[0 for i in range(N)]

    _S=deque(S)
    prevT=_S.popleft()
    for i in range(1,N):
        #T=S[0:i+1]#i=0で一字含む, 
        """
        T+=_S.popleft()
        cumsum[i]=T.count("AC")#cumsum[i]:i+1文字以下でACを含むか
        """
        nowT=_S.popleft()
        if(prevT=="A" and nowT=="C"):
            cumsum[i]=cumsum[i-1]+1
        else:
            cumsum[i]=cumsum[i-1]
        prevT=nowT

    cumsum=[0]+cumsum#cumsum[i]:i文字以下でACを含むか
    for j in range(Q):
        print(cumsum[R[j][1]]-cumsum[R[j][0]])

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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()