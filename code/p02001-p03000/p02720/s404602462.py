import sys
from io import StringIO
import unittest


def recursive(base, lunluns):

    lunluns.append(base)

    # 想定される最大値を超える場合何もせず戻る（再帰の終わり)
    if len(base) > 10 or len(base) > 9 and int(base[0]) > 3:
        return
    target = int(base[-1])

    if target is 0:
        add_num = ["0", "1"]
    elif target is 9:
        add_num = ["8", "9"]
    else:
        add_num = [str(target - 1), str(target), str(target+1)]

    for i in add_num:
        recursive("".join(base + str(i)), lunluns)


def resolve():

    k = int(input())

    # 1桁は全てルンルンNoなので、初期値に設定(0も加えておくことで、kと数え方を合わせる)
    lunluns = ["0"]

    # 再帰的処理
    for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        recursive(i, lunluns)

    lunluns = list(map(int, lunluns))
    lunluns.sort()

    print(lunluns[k])


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
        input = """15"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """13"""
        output = """21"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000"""
        output = """3234566667"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()