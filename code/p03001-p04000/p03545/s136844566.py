import sys
from itertools import accumulate

def resolve():
        input = sys.stdin.readline
        S=list(input().rstrip())
        n=3
        for i in range(2**n):
            sum=int(S[0])
            for j in range(n):
                if((i>>j)&1):
                    sum+=int(S[j+1])
                else:
                    sum-=int(S[j+1])
            if(sum==7):
                ans=(S[0]+str((i>>0)&1).replace("1","+").replace("0","-")+S[1]
                +str((i>>1)&1).replace("1","+").replace("0","-")+S[2]+str((i>>2)&1).replace("1","+").replace("0","-")+S[3]
                +"="+str(sum))
                print(ans)
                return
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
        input = """1222"""
        output = """1+2+2+2=7"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """0290"""
        output = """0-2+9+0=7"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3242"""
        output = """3+2+4-2=7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()