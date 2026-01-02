import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def cut(A, k, size) -> bool:
    cnt = 0
    for a in A:
        cnt += a // size
        if a % size == 0:
            cnt -= 1
        if cnt > k:
            return False
    if cnt <= k:
        return True


def main():
    n, k = input_int_list()
    A = input_int_list()

    left = 0
    right = max(A)

    while right > left + 1:
        mid = (left + right) // 2
        res = cut(A, k, mid)
        if res:
            right = mid
        else:
            left = mid
    print(right)
    return


if __name__ == "__main__":
    main()
