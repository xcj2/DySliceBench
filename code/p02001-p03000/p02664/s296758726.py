import sys
from io import StringIO
import unittest

def resolve():
    t = input()

    len_t = len(t)

    ans = []
    set_p = False
    # 探索
    for i in range(len_t):
        if t[i] is "?":
            if i is 0:
                ans.append("D")
            elif len_t-1 is i:
                ans.append("D")
            elif ans[i-1] is "P":
                ans.append("D")
            elif t[i+1] is "D" or t[i+1] is "?":
                ans.append("P")
            else:
                ans.append("D")
        else:
            ans.append(t[i])

    print("".join(ans))




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
        input = """PD?D??P"""
        output = """PDPDPDP"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """P?P?"""
        output = """PDPD"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """?????"""
        output = """DPDPD"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """?DDD??"""
        output = """DDDDPD"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """?DPP??P??"""
        output = """DDPPDDPDD"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """??????D?"""
        output = """DPDPDPDD"""
        self.assertIO(input, output)

    def test_入力例_7(self):
        input = """???????"""
        output = """DPDPDPD"""
        self.assertIO(input, output)

    def test_入力例_8(self):
        input = """??P?PP??"""
        output = """DDPDPPDD"""
        self.assertIO(input, output)

    def test_入力例_9(self):
        input = """??P?D?PP?D"""
        output = """DPDPDPDD"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
