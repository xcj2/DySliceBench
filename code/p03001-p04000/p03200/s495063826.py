import sys
sys.setrecursionlimit(10000000)

#const
dxdy=((1,0),(0,1))
#my functions here!
def pin(type=int):
    return map(type,input().rstrip().split())


#your code here!
def resolve():
    S=input()
    ans=0
    
    hidari=0
    for i,c in enumerate(S):
        if c=="W":
            ans+=i-hidari
            hidari+=1
    print(ans)

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
        input = """BBW"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """BWBWBW"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    #unittest.main()


    resolve()#and submit 2 atcoder!

