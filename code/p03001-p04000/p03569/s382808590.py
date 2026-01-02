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


# 回文判定
def judge(s):
    news = ""
    for si in s:
        if si != 'x':
            news += si

    if news == news[::-1]:
        return True
    else:
        return False

# 操作の最小値
def min_insertion(s):
    news = ""
    for si in s:
        if si != 'x':
            news += si

    n = len(news)
    fir = [0] * ((n + 1)//2)
    lat = [0] * ((n + 1) // 2)

    # 前半
    cursor = 0
    for si in s:
        if si == 'x':
            fir[cursor] += 1
        else:
            cursor += 1

        if cursor == (n+1)//2:
            break

    # 後半
    cursor = 0
    for si in s[::-1]:
        if si == 'x':
            lat[cursor] += 1
        else:
            cursor += 1

        if cursor == (n + 1) // 2:
            break

    ans = 0
    for firi, lati in zip(fir, lat):
        ans += abs(firi - lati)

    return ans


# 入力
s = ns()

# x以外の回文判定
is_kaibun = judge(s)

# 回文でないならおわり
# 回文ならば最小値出す
if is_kaibun:
    if len(set(list(s))) == 1:
        print(0)
    else:
        print(min_insertion(s))
else:
    print(-1)
