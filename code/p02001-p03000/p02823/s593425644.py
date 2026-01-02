import sys
from collections import deque


def resolve():
    input = sys.stdin.readline
    N,A,B=map(int,input().rstrip().split())

    if (B-A)%2==0:
        p1=(B-A)//2
        #p2=min(B-1,N-A)
        #print(min(p1,p2))
        print(int(p1))
    else:
        #p1=(min(int(B-1),int(N-A)))
        """
        if B-1>N-A:
            bufA=N-B+1
            bufB=N-A+1
            A=bufA
            B=bufB
        """
#        if B-1<N-A:
        #if (B-(A-1+1)-1)%2==0:
            #ans=int(A+int((B-(A-1+1)-1)/2))
        #ans=int(min(A-1,N-B)+1+(B-A-1)/2)
        ans=min(A-1,N-B)+1+(B-A-1)//2
    
        print(int(ans))

"""
        else:
            if (A-(B-N+1)-1)%2==0:
                ans=int(N-B+1+(N-(A+(N-B+1)))/2)
                ans=min(ans,N-A)
            else:
                ans=N-A
"""

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
        input = """5 2 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 2 3"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()