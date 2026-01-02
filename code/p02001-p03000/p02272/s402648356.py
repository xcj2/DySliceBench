import math


def merge(S, left, mid, right) -> int:
    # n1 = mid - left
    # n2 = right - mid
    L = S[left: mid]
    R = S[mid: right]

    # for i in range(n1):
    #     L.append(S[left + i])
    L.append(math.inf)

    # for i in range(n2):
    #     R.append(S[mid + i])
    R.append(math.inf)

    i = 0
    j = 0

    for k in range(left, right):
        if L[i] <= R[j]:
            S[k] = L[i]
            i += 1
        else:
            S[k] = R[j]
            j += 1

    return right - left


def merge_sort(S, left, right):
    count = 0

    if left + 1 < right:
        mid = int((left + right) / 2)
        count += merge_sort(S, left, mid)
        count += merge_sort(S, mid, right)
        count += merge(S, left, mid, right)

    return count


def main():
    n = int(input())
    S = list(map(int, input().split()))
    count = 0

    count = merge_sort(S, 0, n)

    print(*S)
    print(count)


if __name__ == "__main__":
    main()

