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
        input = """5 1
00010"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """14 2
11101010110011"""
        output = """8"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1 1
1"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
    (N,K) = (int(i) for i in input().split())
    S=input()
    l=[]
    flg=False
    if S[0]=='0':
        l.append([0,0])
    for i in range(len(S)):
        if flg==True and S[i]=='0':
            l[-1].append(i)
            flg=False
        if flg==False and S[i]=='1':
            l.append([i])
            flg=True
    if S[-1]=='0':
        l.append([len(S),len(S)])
    else:
        l[-1].append(len(S))
    if K>=len(l)-1:
        print(len(S))
        return()

    print(max( [ l[i+K][1]-l[i][0] for i in range(len(l)-K)] ) )
       

if __name__ == "__main__":
    resolve()