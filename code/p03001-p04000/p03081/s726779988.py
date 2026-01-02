# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n, q = LI()
    S = SI()

    Q = [LS() for _ in range(q)]

    def left_out(i):
        if i < 0: return True
        if i >= n: return False
        for t, d in Q:
            if t != S[i]: continue
            if d == 'L':
                i -= 1
                if i < 0: return True
            else:
                i += 1
                if i >= n: return False

        return False

    def right_out(i):
        if i < 0: return False
        if i >= n: return True
        for t, d in Q:
            if t != S[i]: continue
            if d == 'L':
                i -= 1
                if i < 0: return False
            else:
                i += 1
                if i >= n: return True

        return False

    # 左へ落ちるロボット
    l_ok, l_ng = -1, n
    while abs(l_ok - l_ng) > 1:
        mid = (l_ok + l_ng) // 2
        if left_out(mid):
            l_ok = mid
        else:
            l_ng = mid

    # 右へ落ちるロボット
    r_ok, r_ng = n, -1
    while abs(r_ok - r_ng) > 1:
        mid = (r_ok + r_ng) // 2
        if right_out(mid):
            r_ok = mid
        else:
            r_ng = mid

    return max(0, r_ok - l_ok - 1)


print(main())
