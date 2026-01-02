# -*- coding:utf-8 -*-


def merge(lst, left, mid, right):
    L = lst[left: mid]
    R = lst[mid: right]
    l_len = len(L)
    r_len = len(R)
    i = 0
    j = 0
    cnt = 0
    for k in range(left, right):
        if l_len <= i:
            lst[k] = R[j]
            j += 1
        elif r_len <= j:
            lst[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            cnt += l_len - i
            j += 1
    return cnt


def mergeSort(lst, left, right):
    if left + 1 < right:
        mid = (left + right) >> 1
        cnt = mergeSort(lst, left, mid)
        cnt += mergeSort(lst, mid, right)
        return merge(lst, left, mid, right) + cnt
    else:
        return 0


def inversions(lst, n):
    return mergeSort(lst, 0, n)


def countingSort(lst, n):
    cnt_lst = [0] * (max(lst)+1)

    for i in range(0, n):
        cnt_lst[lst[i]] += 1

    i = 0
    result = []
    for j, cnt in enumerate(cnt_lst):
        for _ in range(0, cnt):
            result.append(j)
    return result


if __name__ == "__main__":
    n = int(input())
    lst = [int(val) for val in input().split()]
    print(inversions(lst, n))