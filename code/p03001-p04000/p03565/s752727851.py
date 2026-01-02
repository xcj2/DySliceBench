import sys
from io import StringIO
import unittest

def resolve():
    S = input()
    T = input()

    S = list(S[::-1])
    T = list(T[::-1])

    flag = 0
    for i in range(0, len(S) - len(T) + 1):
        # Tが当てはまるかどうかの判定
        cnt = 0
        for j in range(len(T)):
            if S[i + j] == T[j] or S[i + j] == '?':
                cnt += 1

        if cnt == len(T):
            for j in range(len(T)):
                S[i + j] = T[j]
            flag = 1
            break

    if flag == 0:
        print('UNRESTORABLE')
        exit(0)

    for i in range(len(S)):
        if S[i] == '?':
            S[i] = 'a'

    S.reverse()
    print(''.join(S))


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
        input = """?tc????
coder"""
        output = """atcoder"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """??p??d??
abc"""
        output = """UNRESTORABLE"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()