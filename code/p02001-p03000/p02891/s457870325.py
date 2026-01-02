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

s = ns()
n = len(s)
kind = len(set(list(s)))
k = ni()

if n == 1:
    print(k // 2)
elif kind == 1:
    print(n*k // 2)
else:
    # 2個つなげる
    s2 = s + s

    # 前半、後半の変える場所を記録
    prev = ""
    flag = True
    fst = 0
    lat = 0
    for i, si in enumerate(s2):
        if si == prev:
            if flag:
                if i < n:
                    fst += 1
                else:
                    lat += 1
                flag = False

            else:
                flag = True
        else:
            flag = True

        prev = si

    print(fst + lat * (k-1))
