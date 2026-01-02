from typing import List


def count_loadable_baggage_num(baggage_num: int, truck_num: int, baggages: List[int], truck_capacity: int) -> int:
    loaded_baggage_num: int = 0

    for _ in range(truck_num):
        current_weight: int = 0
        while current_weight + baggages[loaded_baggage_num] <= truck_capacity:
            current_weight += baggages[loaded_baggage_num]
            loaded_baggage_num += 1
            if loaded_baggage_num == baggage_num:
                return baggage_num

    return loaded_baggage_num


def calc_turck_min_capacity(baggage_num: int, truck_num: int, baggages: List[int]) -> int:
    ng: int = max(baggages) - 1
    ok: int = sum(baggages) + 1

    while ok - ng > 1:
        mid = (ng + ok) // 2
        loadable_baggage_num = count_loadable_baggage_num(baggage_num, truck_num, baggages, mid)
        if loadable_baggage_num >= baggage_num:
            ok = mid
        else:
            ng = mid

    return ok


def main():
    n, k = map(int, input().split())
    w: List[int] = []

    for _ in range(n):
        w.append(int(input()))

    P = calc_turck_min_capacity(n, k, w)
    print(P)


if __name__ == "__main__":
    main()

