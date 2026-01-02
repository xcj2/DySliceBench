#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return [LIST() for _ in range(n)]


INF = float("inf")
MOD = 10**9 + 7


def main():
    from bisect import bisect_left, bisect_right
    N, K = MAP()
    A = LIST()
    A.sort()
    neg = bisect_left(A, 0)
    pos = bisect_right(A, 0)
    negative = A[:neg]
    zeros = A[neg:pos]
    positive = list(reversed(A[pos:]))
    if len(negative) + len(positive) < K:
        # 必ず0を選ぶ必要がある
        print(0)
        return
    if len(positive) == 0:
        if K % 2 == 1:
            if len(zeros) > 0:
                # 0を選びさえすれば良い
                print(0)
                return
            else:
                # 負の数から、0に近い数を選ぶ
                ans = 1
                for n in negative[-K:]:
                    ans *= (-n)
                    ans %= MOD
                ans *= -1
                print(ans % MOD)
                return
        else:
            # 答えは正となる。絶対値が大きい数を選ぶ
            ans = 1
            for n in negative[:K]:
                ans *= (-n)
                ans %= MOD
            print(ans % MOD)
            return

    if len(negative) + len(positive) == K:
        if len(negative) % 2 == 1:
            if len(zeros) > 0:
                print(0)
                return
            else:
                ans = 1
                for a in A:
                    ans *= a
                    ans %= MOD
                print(ans % MOD)
                return
    # print(negative)
    # print(zeros)
    # print(positive)
    # 負の数は二個一で採用する
    new_neg = []
    for i in range(0, len(negative)-1, 2):
        new_neg.append(negative[i]*negative[i+1])

    phead = 0
    nhead = 0

    k = K
    ans = 1
    while k > 1 and phead+2 < len(positive) and nhead < len(new_neg):
        if k >= 3:
            # 負のやつと、正の２番め３番目の積を比較する
            if new_neg[nhead] < positive[phead+1]*positive[phead+2]:
                ans *= positive[phead]
                ans %= MOD
                phead += 1
                k -= 1
                continue
            else:
                ans *= new_neg[nhead]
                ans %= MOD
                nhead += 1
                k -= 2
                continue
        if k == 2:
            if new_neg[nhead] < positive[phead+1]*positive[phead]:
                ans *= positive[phead+1]*positive[phead]
                ans %= MOD
                print(ans)
                return
            else:
                ans *= new_neg[nhead]
                ans %= MOD
                print(ans)
                return
    if nhead >= len(new_neg):
        # 残りは正から採用する
        # ここではpositiveは尽きない
        while k > 0:
            ans *= positive[phead]
            ans %= MOD
            phead += 1
            k -= 1
        print(ans)
        return
    if phead + 2 >= len(positive):
        # positiveが残り1個か2個
        if k % 2 == 0:
            # 負からとるんだが、残りのpositiveが2つなら、それを一回だけ代わりに使える
            pcand = -INF
            if phead + 1 < len(positive):
                pcand = positive[phead]*positive[phead+1]

            while k > 1 and nhead < len(new_neg):
                ncand = new_neg[nhead]
                if ncand < pcand:
                    ans *= pcand
                    ans %= MOD
                    pcand = -INF
                    k -= 2
                else:
                    ans *= ncand
                    ans %= MOD
                    nhead += 1
                    k -= 2
            if k != 0:
                ans *= pcand
                ans %= MOD

            print(ans % MOD)
            return
        else:
            # print(k)
            # print(positive[phead:])
            # print(new_neg[nhead:])
            ans *= positive[phead]
            ans %= MOD
            while k > 1:
                ncand = new_neg[nhead]
                ans *= ncand
                ans %= MOD
                k -= 2
                nhead += 1
            print(ans)
            return
    if k == 1:
        ans *= positive[phead]
        ans %= MOD
        print(ans)
        return
    #
    # 負の個数、0の個数,正の個数
    # 負の個数+正の個数 < Kの場合、0
    # 正の個数 == 0の場合、
    #   Kが奇数なら、0か0に近いものをK個
    #   Kが偶数なら、大きい物をK個
    # 0 < 正の個数 <= K の場合、
    #   いくつ負を選ぶかという話 二個一で貪欲 最後は最大の正
    return


if __name__ == '__main__':
    main()
