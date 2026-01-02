import sys

n, truck_num = map(int, input().split())
weights = [int(x) for x in map(int, sys.stdin)]


def main():
    # 最小値と最大値をもとに二分探索する
    print(binary_search(max(weights), sum(weights)))


def binary_search(left, right):
    """二分探索

    :param left: 最小値
    :param right: 最大値
    :return:
    """

    while left < right:
        # 真ん中の値を割り当てる
        middle = (left + right) // 2

        # 真ん中の値で一旦シミュレート
        if simulate(middle, weights, truck_num):
            # OKならば、最大値をシミュレートした値に
            right = middle
        else:
            # NGならば、最小値をシミュレートした+1に
            left = middle + 1

    return left


def simulate(mid, wei, t_num):
    """

    :param mid: 中央値
    :param wei: 荷物が格納されたリスト
    :param t_num: トラックの台数
    :return: シミュレートOKかNGか
    """
    count = 1
    tmp = 0
    for w in wei:
        tmp += w

        # 積載量(tmp)が求める答え(mid)より大きくなったら
        if mid < tmp:
            # tmpを次の積載物に初期化
            tmp = w
            count += 1
            if t_num < count:
                return False
    return True


if __name__ == '__main__':
    main()


