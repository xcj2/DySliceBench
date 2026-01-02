"""
LRとUDは独立に考えて良い
"""

import unittest


def main():
    H, W, N = map(int, input().split())

    sr, sc = map(int, input().split())

    S = input()
    T = input()

    print(solve(H, W, N, sr, sc, S, T))


def pp(c,s):
    # print(c,''.join(['+' if c == 1 else '-' if c == -1 else ' ' for c in s]))
    return True


def solve(h, w, n, sr, sc, s, t):
    s_lr = []
    s_ud = []
    for c in s[::-1]:
        if c == 'L':
            s_lr.append(-1)
            s_ud.append(0)
        elif c == 'R':
            s_lr.append(+1)
            s_ud.append(0)
        elif c == 'U':
            s_lr.append(0)
            s_ud.append(-1)
        elif c == 'D':
            s_lr.append(0)
            s_ud.append(+1)

    t_lr = []
    t_ud = []
    for c in t[::-1]:
        if c == 'L':
            t_lr.append(-1)
            t_ud.append(0)
        elif c == 'R':
            t_lr.append(+1)
            t_ud.append(0)
        elif c == 'U':
            t_lr.append(0)
            t_ud.append(-1)
        elif c == 'D':
            t_lr.append(0)
            t_ud.append(+1)

    if aoki_win(n, s_ud, t_ud, h, sr) and aoki_win(n, s_lr, t_lr, w, sc):
        return 'YES'
    else:
        return 'NO'


def aoki_win(n, chokudai, aoki, l, sp):
    """
    最後から範囲を削っていく
    """
    # print(l, sp)
    pp('AO', aoki)
    pp('CH',chokudai)

    chokudai_minus = 0
    chokudai_plus = 0
    for c in chokudai:
        if c == 1:
            chokudai_plus += 1
        elif c == -1:
            chokudai_minus += 1
    if 1 <= sp-chokudai_minus and sp+chokudai_plus <= l:
        # print('#1')
        return True
    chokudai_right = l if chokudai[0] == 1 else l+1
    chokudai_left = 1 if chokudai[0] == -1 else 0
    # aoki_right = chokudai_right -1
    # aoki_left = chokudai_right + 1

    for i in range(1, n):
        # print(chokudai_left,']','[', chokudai_right)
        if aoki[i] == 1:
            # aoki_left = max(aoki_left-1, 1)
            chokudai_left = max(0, chokudai_left-1)
        elif aoki[i] == -1:
            # aoki_right = min(aoki_right+1, l)
            chokudai_right = min(l+1, chokudai_right+1)
        if chokudai_left+1 >= chokudai_right:
            # print('#2')
            # print(chokudai_left,']','[', chokudai_right)
            return False
        if chokudai[i] == 1:
            chokudai_right = max(chokudai_right-1, 1)
        elif chokudai[i] == -1:
            chokudai_left = min(chokudai_left+1, l)
        if chokudai_left+1 >= chokudai_right:
            # print('#3')
            # print(chokudai_left,']','[', chokudai_right)
            return False
    
    if sp<=chokudai_left or chokudai_right<=sp:
        # print('#4')
        return False
    
    # print('#5')

    return True

class TestSolve(unittest.TestCase):
    def test_solve_case_1(self):
        h = 2
        w = 3
        n = 3
        sr = 2
        sc = 2
        s = 'RRL'
        t = 'LUD'
        actual = solve(h,w,n,sr,sc,s,t)
        expected = 'YES'
        self.assertEqual(expected, actual)

    def test_solve_case_2(self):
        h = 4
        w = 3
        n = 5
        sr = 2
        sc = 2
        s = 'UDRRR'
        t = 'LLDUD'
        actual = solve(h,w,n,sr,sc,s,t)
        expected = 'NO'
        self.assertEqual(expected, actual)

    def test_solve_case_3(self):
        h = 5
        w = 6
        n = 11
        sr = 2
        sc = 1
        s = 'RLDRRUDDLRL'
        t = 'URRDRLLDLRD'
        actual = solve(h,w,n,sr,sc,s,t)
        expected = 'NO'
        self.assertEqual(expected, actual)

    def test_solve_case_4(self):
        h = 1
        w = 3
        n = 6
        sr = 1
        sc = 2
        s = 'LRRRRR'
        t = 'LRLLRL'
        actual = solve(h,w,n,sr,sc,s,t)
        expected = 'NO'
        self.assertEqual(expected, actual)

    def test_solve_case_5(self):
        h = 1
        w = 3
        n = 4
        sr = 1
        sc = 2
        s = 'LLLL'
        t = 'RRRR'
        actual = solve(h,w,n,sr,sc,s,t)
        expected = 'YES'
        self.assertEqual(expected, actual)

    def test_solve_case_6(self):
        h = 3
        w = 2
        n = 4
        sr = 2
        sc = 2
        s = 'UDLUU'
        t = 'DRRRR'
        actual = solve(h,w,n,sr,sc,s,t)
        expected = 'NO'
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
