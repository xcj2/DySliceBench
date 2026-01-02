import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    def solve_negative():
        ok = -1
        ng = -(10 ** 18)
        a_neg_desc = a_neg[::-1]
        a_pos_desc = a_pos[::-1]

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            pidx = 0
            count = 0
            for elem_neg in a_neg_desc:
                while pidx < pos_cnt:
                    elem_pos = a_pos_desc[pidx]
                    prod = elem_neg * elem_pos
                    if prod > mid:
                        break
                    else:
                        pidx += 1
                count += pidx
            if count >= k:
                ok = mid
            else:
                ng = mid

        print(ok)

    def solve_positive():
        kp = k - (prod_neg_cnt + prod_zer_cnt)
        ok = 10 ** 18
        ng = 0
        a_neg_desc = a_neg[::-1]
        a_pos_desc = a_pos[::-1]

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            pidx = 0
            nidx = 0
            count = 0
            for i, elem_pos1 in enumerate(a_pos_desc):
                while pidx < pos_cnt:
                    elem_pos2 = a_pos[pidx]
                    prod = elem_pos1 * elem_pos2
                    if prod > mid:
                        break
                    else:
                        pidx += 1
                count += min(pidx, pos_cnt - (i + 1))

            for i, elem_neg1 in enumerate(a_neg):
                while nidx < neg_cnt:
                    elem_neg2 = a_neg_desc[nidx]
                    prod = elem_neg1 * elem_neg2
                    if prod > mid:
                        break
                    else:
                        nidx += 1
                count += min(nidx, neg_cnt - (i + 1))

            if count >= kp:
                ok = mid
            else:
                ng = mid

        print(ok)

    import bisect
    n, k = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    a.sort()

    neg_cnt = bisect.bisect_left(a, 0)
    zer_cnt = bisect.bisect_left(a, 1) - neg_cnt
    pos_cnt = n - (neg_cnt + zer_cnt)

    prod_neg_cnt = neg_cnt * pos_cnt
    prod_pos_cnt = (neg_cnt * (neg_cnt - 1) + pos_cnt * (pos_cnt - 1)) // 2
    prod_zer_cnt = ((n * (n - 1)) // 2) - (prod_neg_cnt + prod_pos_cnt)

    a_neg = a[:neg_cnt]
    a_pos = a[(n - pos_cnt):]

    if k <= prod_neg_cnt:
        solve_negative()
    elif k <= (prod_neg_cnt + prod_zer_cnt):
        print(0)
    else:
        solve_positive()


if __name__ == '__main__':
    main()
