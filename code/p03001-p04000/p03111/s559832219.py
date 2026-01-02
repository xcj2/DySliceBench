import sys
input = sys.stdin.readline
N,A,B,C=map(int,input().rstrip().split())
l=[int(input().rstrip()) for _ in range(N)]
inf=10**9+7
def resolve():
    print(rect(0,0,0,0))

def rect(i,a,b,c):
    if i==N:
        if(a==0 or b==0 or c==0):
            return inf
        return abs(A-a)+abs(B-b)+abs(C-c)



    ans=rect(i+1,a,b,c)

    costa=10 if a!=0 else 0
    costb=10 if b!=0 else 0
    costc=10 if c!=0 else 0

    ans=min(ans,rect(i+1,a+l[i],b,c)+costa)
    ans=min(ans,rect(i+1,a,b+l[i],c)+costb)
    ans=min(ans,rect(i+1,a,b,c+l[i])+costc)


    return ans


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
        input = """5 100 90 80
98
40
30
21
80"""
        output = """23"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """8 100 90 80
100
100
90
90
90
80
80
80"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8 1000 800 100
300
333
400
444
500
555
600
666"""
        output = """243"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()