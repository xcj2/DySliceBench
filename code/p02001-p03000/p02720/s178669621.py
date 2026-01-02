from collections import deque


def calc_next_ones_places(last_ones_place):
    """次の Lunlun数 の一の位の数を返す"""
    if last_ones_place == 0:
        return [last_ones_place, last_ones_place+1]
    elif last_ones_place == 9:
        return [last_ones_place-1, last_ones_place]
    else:
        return [last_ones_place-1, last_ones_place, last_ones_place+1]


def calc_k_th_lunlun_num(k):
    """
    Kが10以上の時、K番目のLunlun数を計算する
    """
    lunlun_num_queue = deque()

    for i in range(1, 10):
        lunlun_num_queue.append(i)

    iterate_num = 9
    while True:
        last_lunlun_num = lunlun_num_queue.popleft()
        last_ones_place = str(last_lunlun_num)[-1]
        next_ones_places_list = calc_next_ones_places(int(last_ones_place))
        for next_ones_place in next_ones_places_list:
            lunlun_num = 10*last_lunlun_num + next_ones_place
            lunlun_num_queue.append(lunlun_num)

            iterate_num += 1
            if iterate_num == k:
                return lunlun_num


def main():
    K = int(input())
    if K <= 9:
        print(K)
    else:
        k_th_lunlun_num = calc_k_th_lunlun_num(K)
        print(k_th_lunlun_num)


main()
