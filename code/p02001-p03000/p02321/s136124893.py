def make_combination(fro, to, value, weight, W):
    """ビット演算が重いのでグレイコードを使った"""
    combination = []
    w = 0
    v = 0
    combination.append([w, v])
    for i in range(1, 1 << (to - fro)):
        code = i ^ (i >> 1)
        bitpos = 0
        while not (1 << bitpos & i):
            bitpos += 1
        if (1 << bitpos & code):
            w += weight[bitpos + fro]
            v += value[bitpos + fro]
        else:
            w -= weight[bitpos + fro]
            v -= value[bitpos + fro]
        combination.append([w, v])

    # 必要のない組み合わせを弾く
    combination.sort()
    for i in range(len(combination) - 1):
        if combination[i][1] > combination[i + 1][1]:
            combination[i + 1][1] = combination[i][1]

    return combination


def cal_ans(from_0_to_half_combination, from_half_to_N_combination, W):
    ans = 0

    """ 尺取り法 """
    left = 0
    right = len(from_half_to_N_combination) - 1
    for left in range(len(from_0_to_half_combination)):
        now_weight = from_0_to_half_combination[left][0]
        now_value = from_0_to_half_combination[left][1]
        while now_weight + from_half_to_N_combination[right][0] > W and right != 0:
            right -= 1
        if now_weight + from_half_to_N_combination[right][0] <= W:
            ans = max(ans, now_value + from_half_to_N_combination[right][1])

    """ 二分探索 """
    # for now in range(len(from_0_to_half_combination)):
    #     now_weight = from_0_to_half_combination[now][0]
    #     now_value = from_0_to_half_combination[now][1]
    #     count = 0
    #     left = 0
    #     right = len(from_0_to_half_combination) - 1
    #     while count < 45:
    #         mid = (left + right) // 2
    #         if now_weight + from_half_to_N_combination[mid][0] > W:
    #             right = mid - 1
    #         else:
    #             ans = max(ans, now_value + from_half_to_N_combination[mid][1])
    #             left = mid + 1
    #         count += 1

    return ans


def main():
    N, W = map(int, input().split())
    half = N // 2
    value = []
    weight = []
    for i in range(N):
        v, w = map(int, input().split())
        value.append(v)
        weight.append(w)

    # 半分全列挙の組み合わせを前半と後半で作る
    from_0_to_half_combination = make_combination(0, half, value, weight, W)
    from_half_to_N_combination = make_combination(half, N, value, weight, W)

    # 尺取り法か二分探索で計算
    ans = cal_ans(from_0_to_half_combination, from_half_to_N_combination, W)
    print(ans)


if __name__ == "__main__":
    main()

