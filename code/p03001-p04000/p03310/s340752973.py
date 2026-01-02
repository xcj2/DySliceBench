def d_equal_cut(N, A):
    import itertools
    import bisect

    cumsum = [0] + list(itertools.accumulate(A))  # Aの累積和

    def get_sum(left, right):
        # A[left]~A[right]の総和を得る
        return cumsum[right+1] - cumsum[left]

    def get_optimum_division(left, right):
        # A[left]~A[right]を、前後の総和の差を最小にするように分解する
        total = get_sum(left, right)
        # A[left]~A[right]の総和の半分以上になる要素の要素番号を求める
        # left, right はAの要素番号を指定しているので、
        # cumsumのために[0]をつけた分+1して、最後に-1している
        mid = bisect.bisect_right(
            cumsum, cumsum[left] + total/2, left+1, right+1) - 1

        # midがleftまたはrightと一致しないとき、真ん中の切り方は2通りある
        # (真ん中の要素を左側に入れるか右側に入れるか)ので、
        # 両方計算して差が小さな方を採用する
        diff1, diff2 = float('inf'), float('inf')
        if mid != left:
            sum_L1 = get_sum(left, mid-1)
            sum_R1 = get_sum(mid, right)
            diff1 = abs(sum_L1 - sum_R1)
        if mid != right:
            sum_L2 = get_sum(left, mid)
            sum_R2 = get_sum(mid+1, right)
            diff2 = abs(sum_L2 - sum_R2)
        return [sum_L1, sum_R1] if diff1 <= diff2 else [sum_L2, sum_R2]

    # 真ん中の区切りを全通り試す
    ans = float('inf')
    # 0~mid_cut番の要素を「左側」、mid_cut~N-1番の要素を「右側」とする
    # Aの1番からN-3番までが「左と右を分ける仕切り」になれる
    # (0, N-2, N-1番をその仕切りにすると、空な部分列ができてしまう)
    for mid_cut in range(1, (N-3) + 1):
        total = []
        total.extend(get_optimum_division(0, mid_cut))
        total.extend(get_optimum_division(mid_cut+1, N-1))
        ans = min(ans, abs(max(total) - min(total)))
    return ans

N = int(input())
A = [int(i) for i in input().split()]
print(d_equal_cut(N, A))