# abc147_c.py
import sys
import time
import unittest
from io import StringIO

# IS_LOCAL = True  # FIXME: delete this


def resolve():
    N = int(input())
    aa = []
    for i in range(N):
        xy = {}
        aa.append(xy)
        for _ in range(int(input())):
            x, y = [int(i) for i in input().split()]
            xy[x - 1] = 1 == y
    maxsum = 0
    for comb in range(2**N - 1, -1, -1):
        sum = 0
        for i in range(N):
            if (comb >> i) & 1:
                sum += 1
                for x in aa[i].keys():
                    if aa[i][x]:
                        if not ((comb >> x) & 1):
                            break
                    else:
                        if (comb >> x) & 1:
                            break
                else:
                    continue
                break
        else:
            maxsum = max(maxsum, sum)
    print(maxsum)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def checkTLE(self, input):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin

    def debugIO(self, input):
        stdin = sys.stdin
        sys.stdin = StringIO(input)
        resolve()
        sys.stdin = stdin

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t), flush=True)

    def test_入力例_1(self):
        input = """3
1
2 1
1
1 1
1
2 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1
2 0
1
1 0"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    if "IS_LOCAL" in locals():
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        unittest.TextTestRunner(verbosity=0).run(suite)
    else:
        resolve()
