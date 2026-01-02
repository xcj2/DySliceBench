# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def fi(): return float(input())
def mfi(): return map(float, input().rstrip().split())
def lmfi(): return list(map(float, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template


def main():
    t1, t2 = mi()
    a1, a2 = mi()
    b1, b2 = mi()
    aoki = 0
    taka = 0
    meetF = False
    meetS = False
    # a の方が速くなるようにスワップ
    if t1 * a1 + t2 * a2 < t1 * b1 + t2 * b2:
        x1, x2 = a1, a2
        a1, a2 = b1, b2
        b1, b2 = x1, x2
    # print(a1, a2, b1, b2)
    if t1 * a1 + t2 * a2 == t1 * b1 + t2 * b2:
        exit("infinity")
    if a1 > b1:
        meetF = False
    else:
        meetF = True
    # 1区間目も2区間目もaの法が速いなら合うことはない
    if not meetF:
        exit(0)
    sa = t1 * a1 + t2 * a2 - t1 * b1 - t2 * b2  # 1区切りごとにＡが速く，付いてしまう差
    # print(sa)
    # 何区切りすると追いつけない差になってしまうか
    ng = 10**18
    ok = 1
    while(ng - ok > 1):
        mid = (ng + ok) // 2
        # シミュレーション（mid区切りのあと追いつけるか）
        a = 0
        b = -mid * sa
        if(a + t1 * a1 <= b + t1 * b1):
            ok = mid
        else:
            ng = mid
    # シミュレーション(ok*2回は確実に会う)
    cnt = 2 * (ok - 1) - 1
    a = 0
    b = -(ok - 1) * sa
    for i in range(ok - 1, ok + 10):
        a += t1 * a1
        b += t1 * b1
        if a < b:
            cnt += 2
        if a == b:
            cnt += 1
        a += t2 * a2
        b += t2 * b2
    print(cnt)
    # exit(2 * ok + 1)
    return


if __name__ == '__main__':
    main()
