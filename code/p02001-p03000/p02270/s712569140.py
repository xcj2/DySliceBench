# -*- coding: utf-8 -*-

def bs(n, k, W):
    left, right = max(W), sum(W)
    mid = 0
    while left < right:
        mid = left + (right - left) // 2
        if is_enough(mid, k, W):
            right = mid
        else:
            left = mid + 1
    return left

def is_enough(p, k, W):
    trk_cnt = 1
    weight = 0
    for i in W:
        weight += i
        if weight > p:
            trk_cnt += 1
            weight = i
            if trk_cnt > k:
                return False
    return True

def main():
    n, k = map(int, input().split())
    W = [int(input()) for _ in range(n)]
    rslt = bs(n, k, W)
    print(rslt)

if __name__ == '__main__':
    main()
