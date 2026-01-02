import sys
from io import StringIO
import unittest

from collections import Counter

def resolve():
    n = int(input())
    l = [input() for _ in range(n)]
    cnt = 0
    ee = dict()

    for ll in l:
        tmp = ''.join(sorted(ll))

        if tmp in ee.keys():
            cnt += ee[tmp]
            ee[tmp] += 1
        else:
            ee[tmp] = 1

    print(cnt)

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
        input = """3
acornistnt
peanutbomb
constraint"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
oneplustwo
ninemodsix"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
