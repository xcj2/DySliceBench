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

debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    N, K = LI()
    a_list = LI()
    f_list = LI()

    # 答えで二分探索

    low = 0
    maxa = max(a_list)
    maxf = max(f_list)
    high = (maxa * maxf * N) + 1

    # 妥当な割り当て
    a_list = sorted(a_list)
    f_list = sorted(f_list, reverse=True)
    import math

    dprint(a_list)
    dprint(f_list)

    def judge(ans):
        # ans を答えにできるか
        cnt = 0
        for i in range(N):
            a = a_list[i]
            f = f_list[i]
            if a*f > ans:
                # 差分を訓練で埋める
                ki = math.ceil((a*f - ans) / f)
                cnt += ki
                if cnt > K:
                    dprint('False', ans, cnt)
                    return False
        dprint('True', ans, cnt)
        return True

    while low < high:
        mid = math.floor((low + high) / 2)

        guess = judge(mid)
        # dprint(high, low, mid, guess)

        if guess == True:
            # できるので、これより1少ないのが最大
            high = mid
        else:
            # できないので、これより大きい
            low = mid + 1
        # dprint(high, low)
    print(low)


solve()