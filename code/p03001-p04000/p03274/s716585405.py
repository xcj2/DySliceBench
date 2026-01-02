import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    N, K = LI()
    x_li = LI()  # sorted

    from bisect import bisect_left
    zeropoint = bisect_left(x_li, 0)

    x_negative = [-x for x in reversed(x_li[:zeropoint])]
    x_positive = x_li[zeropoint:]

    # はじめに正の方向に動くとき：
    if len(x_positive) > 0:
        if len(x_positive) >= K:
            pos_right = K-1
            pos_left = 0
            min_moves = x_positive[pos_right]
        else:
            pos_right = len(x_positive) - 1
            pos_left = K - len(x_positive) - 1
            min_moves = x_negative[pos_left] + x_positive[pos_right] * 2
        i = 0
        while True:
            i += 1
            if pos_left + i >= len(x_negative) or pos_right-i < 0: break
            moves = x_negative[pos_left+i] + x_positive[pos_right-i] * 2
            min_moves = min(min_moves, moves)
    else:
        min_moves = INF

    # はじめに負の方向に動くとき：
    if x_positive and x_positive[0] == 0:
        x_positive = x_positive[1:]
        x_negative = [0] + x_negative
    x_positive, x_negative = x_negative, x_positive

    if len(x_positive) > 0:
        if len(x_positive) >= K:
            pos_right = K-1
            pos_left = 0
            min_moves = min(min_moves, x_positive[pos_right])
        else:
            pos_right = len(x_positive) - 1
            pos_left = K - len(x_positive) - 1
            min_moves = min(min_moves, x_negative[pos_left] + x_positive[pos_right] * 2)
        i = 0
        while True:
            i += 1
            if pos_left + i >= len(x_negative) or pos_right-i < 0: break
            moves = x_negative[pos_left+i] + x_positive[pos_right-i] * 2
            min_moves = min(min_moves, moves)
    else:
        pass


    print(min_moves)

main()