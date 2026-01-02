from typing import Set, List


def linear_search_v1(S: List[int], key: int) -> int:
    for num in S:
        if num == key:
            return 1
    return 0


def linear_search_v2(S: List[int], key: int) -> int:
    i: int = 0
    S.append(key)

    while S[i] != key:
        i += 1

    if i != len(S) - 1:
        return 1
    else:
        return 0


def main_v1():
    _ = input()
    S: List[int] = list(map(int, input().split()))
    _ = input()
    T: List[int] = list(map(int, input().split()))
    count: int = 0

    for num in T:
        # count += linear_search_v1(S, num)
        count += linear_search_v2(S[:], num)

    print(count)


def main_v2():
    _ = input()
    S: Set[int] = set(map(int, input().split()))
    _ = input()
    T: List[int] = list(map(int, input().split()))
    count: int = 0

    for num in T:
        if num in S:
            count += 1

    print(count)


if __name__ == "__main__":
    main_v2()

