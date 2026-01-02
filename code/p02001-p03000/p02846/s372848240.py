import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from math import ceil

t1, t2 = li()
a1, a2 = li()
b1, b2 = li()

# 交互になる
if (b1 - a1) * t1 + (b2 - a2) * t2 == 0:
    print('infinity')

# 高橋君が先を行く
elif (b1 - a1) * t1 + (b2 - a2) * t2 < 0:
    # ずっと高橋君の方が速い
    if (b1 - a1) * t1 < 0 and (b2 - a2) * t2 < 0:
        print(0)
    # T2分間は追いつかれる
    elif (b1 - a1) * t1 < 0 and (b2 - a2) * t2 > 0:
        print(0)
    # T1分間は追いつかれる
    else:
        cross = ceil((b1-a1)*t1 / ((a1-b1)*t1 + (a2-b2)*t2)) - 1
        #print(((b1-a1)*t1 + (b2-a2)*t2) * (cross+1) + (a1-b1)*t1)
        if ((a1-b1)*t1 + (a2-b2)*t2) * (cross+1) + (a1-b1)*t1 == 0:
            print(2* (cross+ 1))
        else:
            print(2 * cross + 1)

# 高橋君が遅れる
else:
    # ずっと高橋君のほうが遅い
    if (b1 - a1) * t1 > 0 and (b2 - a2) * t2 > 0:
        print(0)
    # T2分間は追い上げる
    elif (b1 - a1) * t1 > 0 and (b2 - a2) * t2 < 0:
        print(0)
    # T1分間は追い上げる
    else:
        cross = ceil((b1-a1)*t1 / ((a1-b1)*t1 + (a2-b2)*t2)) - 1
        #print(((a1-b1)*t1 + (a2-b2)*t2) * (cross+1) + (a1-b1)*t1)
        if ((a1-b1)*t1 + (a2-b2)*t2) * (cross+1) + (a1-b1)*t1 == 0:
            print(2 * (cross + 1))
        else:
            print(2 * cross + 1)
