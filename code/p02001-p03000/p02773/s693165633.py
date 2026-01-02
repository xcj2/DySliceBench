import sys
from io import StringIO
import unittest


def resolve():
    N = int(input())
    S = {}
    maxs = 0
    for _ in range(N):
        s = input()
        if s in S.keys():
            S[s] += 1
            maxs = max(maxs, S[s])
        else:
            S[s] = 1
            maxs = max(maxs, S[s])
    # S.keys().sort()
    keys = sorted(S.keys())
    for key in keys:
        if S[key] == maxs:
            print(key)


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
        input = """7
beat
vet
beet
bed
vet
bet
beet"""
        output = """beet
vet"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo"""
        output = """buffalo"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
bass
bass
kick
kick
bass
kick
kick"""
        output = """kick"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
ushi
tapu
nichia
kun"""
        output = """kun
nichia
tapu
ushi"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
