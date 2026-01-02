#!/usr/bin/env python3
import sys

INF = 2 * 10 ** 3 + 1

def main():
    N = int(input())
    L = [int(i) for i in input().split()]
    L.sort()

    # True ---- False
    def is_ok_top(mid: int, a: int, b: int):
        # 検索対象の外にあるものは先に弾く(リストのインデックスなんかだとout of rangeするので)
        if mid < 0:
            return True
        elif mid >= N:
            return False
        return L[mid] < L[a] + L[b]

    def binSearch_top(ok: int, ng: int, a: int, b: int):
        #print(ok, ng)              # はじめの2値の状態
        while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
            mid = (ok + ng) // 2
            if is_ok_top(mid, a, b):
                ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            else:
                ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            #print(ok, ng)          # 半分に切り分ける毎の2値の状態
        return ok    

    count = 0
    for a in range(0, len(L) - 2):
        for b in range(a + 1, len(L) - 1):
            count += binSearch_top(-1, INF, a, b) - b

    print(count)







if __name__ == '__main__':
    main()
