import sys
from io import StringIO
import unittest
import math

def resolve():
    N, =  input().split()
    calc9(N)

# def resolve():
#     N, = map(int, input().split())
#     if N%9==0:
#         print("Yes")
#     else:
#         print("No")

def calc9(n):
    if len(n)==1:
        if n=='9' or n=='0':
            # print(n)
            print("Yes")
        else:
            # print(n)
            print("No")
    else:
        sum =0
        for s in n:
            sum=sum+int(s)
        calc9(str(sum))

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    # def test_入力例_1(self):
    #     input = """123456789"""
    #     output = """Yes"""
    #     self.assertIO(input, output)
    #
    def test_入力例_2(self):
        input = """0"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31415926535897932384626433832795028841971693993751058209749445923078164062862089986280"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    resolve()
