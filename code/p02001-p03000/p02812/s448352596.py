import sys

def resolve():
    input = sys.stdin.readline
    N=int(input().rstrip())
    S=input().rstrip()

    count=0
    buf2=""
    buf1=""
    for i in range(N):
        buf0=S[i]

        if buf2=="A" and buf1=="B" and buf0=="C":
            count+=1
        buf2=buf1
        buf1=buf0
        
    print(count)

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
        input = """10
ZABCDBABCQ"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """19
THREEONEFOURONEFIVE"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """33
ABCCABCBABCCABACBCBBABCBCBCBCABCB"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()