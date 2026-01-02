import sys
from io import StringIO
import unittest

import numpy as np

def resolve():
    a = np.array([list(map(int, input().split())) for _ in range(3)])
    n = int(input())
    b = set([int(input()) for _ in range(n)])
    flag = 0

    for i in range(3):
        if set(a[i]).issubset(b) or set(a[:, i]).issubset(b):
            flag = 1
            break

    if set([a[0][0], a[1][1], a[2][2]]).issubset(b) or set([a[0][2], a[1][1], a[2][0]]).issubset(b):
        flag = 1

    if flag == 1:
        print('Yes')
    else:
        print('No')



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
        input = """84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """41 7 46
26 89 2
78 92 8
5
6
45
16
57
17"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()