"""
ブチギレチューニングタイム
"""
#!/usr/bin/env python3

import sys
from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).



def main():
    def input(): return sys.stdin.readline().rstrip()
    def mi():    return map(int, input().split())
    def lmi():   return list(map(int, input().split()))


    def is_ok(pivot, k, L_positive, L_negative):
        cnt = 0
        ind = 0
        for positive_num in L_positive:
            target = pivot // positive_num
            # O(nlgn) -> O(2 * n) = O(n) に落ちている！
            while ind < len(L_negative):
                if L_negative[ind] <= target:
                    ind += 1
                else:
                    break
            cnt += ind
        # print(f"A pivot {pivot} cnt {cnt} k {k}")
        return cnt >= k


    def is_ok_handle_duplicate(pivot, k, L_positive, L_negative):
        pos_cnt = 0
        ind = len(L_positive)
        if len(L_positive) >= 2:
            for num in L_positive:
                target = pivot // num
                # target 以下の個数を求める
                # O(nlgn) -> O(2 * n) = O(n) に落ちている！
                while ind > 0:
                    if L_positive[ind - 1] > target:
                        ind -= 1
                    else:
                        break
                pos_cnt += ind
                if num ** 2 <= pivot:
                    pos_cnt -= 1
            pos_cnt //= 2
        neg_cnt = 0
        ind = len(L_negative)
        if len(L_negative) >= 2:
            for num in L_negative:
                target = pivot // num
                # target 以下の個数を求める
                # O(nlgn) -> O(2 * n) = O(n) に落ちている！
                while ind > 0:
                    if L_negative[ind - 1] > target:
                        ind -= 1
                    else:
                        break
                neg_cnt += ind
                if num ** 2 <= pivot:
                    neg_cnt -= 1
            neg_cnt //= 2
        cnt = pos_cnt + neg_cnt
        # print(f"B pivot {pivot} cnt {cnt} k {k}")
        return cnt >= k


    n, k = mi()
    L = lmi()
    L.sort()
    l_z = bisect_left(L, 0)
    r_z = bisect_right(L, 0)
    L_negative, L_zero, L_positive = L[:l_z], L[l_z:r_z], L[r_z:]

    num_pairs_negative = len(L_negative) * len(L_positive)
    num_pairs_zero = len(L_zero) * (len(L_zero) -1) // 2 + len(L_zero) * (n - len(L_zero))
    
    if k <= num_pairs_negative:
        """
        積が x 以下となるペアの個数が k 個以上となるような x の範囲が定まる。
        left はその範囲外、right はその範囲内とする。
        """
        # left = - 10 ** 18 - 1
        # 定数倍高速化
        left = L_negative[0] * L_positive[-1] - 1
        # right = 0
        # 定数倍高速化
        right = L_negative[-1] * L_positive[0] + 1
        while right - left > 1:
            mid = (left + right) // 2
            if is_ok(mid, k, L_positive, L_negative):
                right = mid
            else:
                left = mid
        print(right)
    elif k <= num_pairs_negative + num_pairs_zero:
        print(0)
    else:
        """
        積が x 以下となるペアの個数が k 個以上となるような x の範囲が定まる。
        left はその範囲外、right はその範囲内とする。
        """
        k -= (num_pairs_negative + num_pairs_zero)
        L_negative = [- elm for elm in reversed(L_negative)]
        # left = 0
        # 定数倍高速化
        if L_negative and L_positive:
            left = min(L_negative[0] ** 2, L_positive[0] ** 2) - 1
        elif L_negative:
            left = L_negative[0] ** 2 - 1
        else:
            left = L_positive[0] ** 2 - 1
        # right = 10 ** 18 + 1
        # 定数倍高速化
        if L_negative and L_positive:
            right = max(L_negative[-1] ** 2, L_positive[-1] ** 2) + 1
        elif L_negative:
            right = L_negative[-1] ** 2 + 1
        else:
            right = L_positive[-1] ** 2 + 1
        while right - left > 1:
            mid = (left + right) // 2
            if is_ok_handle_duplicate(mid, k, L_positive, L_negative):
                right = mid
            else:
                left = mid
        print(right)
    

if __name__ == "__main__":
    # import time
    # s = time.time()
    main()
    # print(f"elapsed {time.time() - s} sec" )


"""
ローカル環境だと PyPy くんが 1.0 秒くらいで通るケースたちがことごとく TLE なのですが...

トータルで O(60 * nlgn) -> O(60 * n) にしたところ... (lg(10^18) ~ 60)
cat sub1_02.in | pypy3 d.py
> elapsed 1.211238145828247 sec -> elapsed 0.307081937789917 sec
cat sub1_03.in | pypy3 d.py
> elapsed 1.6172709465026855 sec -> elapsed 0.41311001777648926 sec
cat sub1_04.in | pypy3 d.py
> elapsed 0.9529299736022949 sec -> elapsed 0.1954030990600586 sec
cat sub1_08.in | pypy3 d.py
> elapsed 0.7351880073547363 sec -> elapsed 0.19420194625854492 sec
爆速！
"""