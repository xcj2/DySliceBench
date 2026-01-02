import sys
from itertools import accumulate
from itertools import groupby
#from scipy.special import comb
#from scipy.misc import comb

#booltable=[0]+booltable
"""
6
1 3 -4 2 2 -2

3
"""

def resolve():
    #input = sys.stdin.readline
    N=int(input().rstrip())
    #A=list(map(int,input().rstrip().split()))
    A=[int(x)for x in input().split()]


    cumsum = sorted(list(accumulate(A)))
    ans=0
    for key, group in groupby(cumsum):
        groupsize=len(list(group))
        if groupsize>=2:
            #ans += comb(groupsize,2,1) # 組み合わせ列挙 5C3
            ans+=groupsize*(groupsize-1)//2
        if key==0:
            ans+=groupsize
    print(int(ans))        
    


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
        input = """6
1 3 -4 2 2 -2"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7
1 -1 1 -1 1 -1 1"""
        output = """12"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5
1 -2 3 -4 5"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()