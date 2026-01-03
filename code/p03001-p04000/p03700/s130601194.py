# coding: utf-8
import array, bisect, collections, copy, heapq, itertools, math, random, re, string, sys, time

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7


def II(): return int(input())
def ILI(): return list(map(int, input().split()))
def IAI(LINE): return [ILI() for __ in range(LINE)]
def IDI(): return {key: value for key, value in ILI()}


def read():
    N, A, B = ILI()
    h = [II() for __ in range(N)]
    return (N, A, B, h)


def bool_exc(h, dif_ab, B, count):
    dif_count = 0
    for mon in h:
        dif_mon = mon - B * count
        if dif_mon <= 0:
            continue
        else:
            dif_count += math.ceil(dif_mon / dif_ab)
            if dif_count > count:
                break

    dif = count - dif_count
    return dif


def solve(N, A, B, h):
    right = max(h) // B + 1
    left = min(h) // A + 1
    dif_ab = A - B
    while left != right:
        mid = (left + right) // 2
        dif = bool_exc(h, dif_ab, B, mid)
        if dif >= 0:
            right = mid
        else:
            left = mid + 1

    ans = left
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
