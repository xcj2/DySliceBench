import sys
from io import StringIO
import unittest


def resolve():
    tak_hp, tak_ak, ao_hp, ao_ak = map(int, input().split())

    for i in range(9999999999999):
        ao_hp -= tak_ak
        if ao_hp <= 0:
            print("Yes")
            return
        tak_hp -= ao_ak
        if tak_hp <= 0:
            print("No")
            return



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
        input = """10 9 10 10"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """46 4 40 5"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()
