import math
import sys
from io import StringIO
import unittest
from functools import reduce

def resolve():
    k = int(input())

    abc = [0, 0, 0]
    ans = 0

    for i in range(1, k + 1):
        for j in range(k):

            abc[j] = i

            if 0 in abc:
                continue

            work = reduce(math.gcd, abc)
            if not abc[0] == abc[1] == abc[2]:
                work = work * 3
            ans += work
            print(str(abc) + "| " +str(work))

    print(ans)



def not_resolve2():
    k = int(input())

    ans = 0

    for a in range(1, k + 1):
        # print(a)
        for b in range(a, k + 1):
            for c in range(b, k + 1):
                work = reduce(math.gcd, [a, b, c])
                if a == b == c:
                    print("これは×3しない")
                    print(str(a) + "|" + str(b) + "|" + str(c) + "=" + str(work))
                    # ×3しない
                    pass
                else:
                    print("これは×3する")
                    print(str(a) + "|" + str(b) + "|" + str(c) + "=" + str(work * 3))
                    work = work * 3
                ans += work

    print(ans)


# これじゃダメ。タイムアウトする気がする・・。
def not_resolve():
    k = int(input())

    ans = 0

    for a in range(1, k + 1):
        for b in range(1, k + 1):
            for c in range(1, k + 1):
                ans += reduce(math.gcd, [a, b, c])

    print(ans)



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
        input = """2"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例(self):
        input = """3"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """200"""
        output = """10813692"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    not_resolve()
    #not_resolve()
