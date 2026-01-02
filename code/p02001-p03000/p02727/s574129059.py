import sys
from bisect import bisect_right, bisect_left

def to_cumsum(arr, pad=True):
    """
    1次元配列を累積和の1次元配列に変換する
    pad: 先頭に0の項を作る場合はTrue
    """
    cumsum = 0
    padding = 1 if pad else 0
    new = [0] * (len(arr) + padding)
    for i, e in enumerate(arr):
        cumsum += e
        new[i + padding] = cumsum
    return new

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


X, Y, A, B, C = MI()
P = LMI()
Q = LMI()
R = LMI()

P.sort(reverse=True)
Q.sort(reverse=True)

R.extend(P[:X])
R.extend(Q[:Y])

R.sort(reverse=True)
print(sum(R[:X + Y]))