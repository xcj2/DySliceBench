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
    N = II()
    l_list = LI()

    # 短い順
    l_list = sorted(l_list)
    ind_list = list(range(len(l_list)))

    from bisect import bisect_left, bisect_right
    from itertools import combinations
    dprint(l_list)
    cnt = 0
    for a, b in combinations(ind_list, 2):
        # 2つえらぶ

        # 残りでできたl_listを作る
        # cand_list = []
        # for c in range(len(l_list)):
        #     if c != a and c!= b:
        #         cand_list.append(l_list[c])

        # cのmax, min
        la = l_list[a]
        lb = l_list[b]

        mx = la + lb
        mn = max(la, lb) - min(la, lb)

        # cand_listをbisectする
        right_ind_plus1 = bisect_left(l_list, mx)
        left_ind = bisect_right(l_list, mn)

        # dprint(la, lb, mn, mx, l_list, left_ind, right_ind_plus1, cnt)

        cnt += right_ind_plus1 - left_ind

        if left_ind <= a and a < right_ind_plus1:
            cnt -= 1

        if left_ind <= b and b < right_ind_plus1:
            cnt -= 1

    print(cnt//3)

solve()