#!/usr/bin/env python3

def solve_m(S, T, K):
    def count(x):
        ret, ti = 0, 0
        for s in S:
            # 積がxを初めて下回るtiを求める。なければlen(T)
            while ti < len(T) and s * T[ti] > x:
                ti += 1
            if ti == len(T):
                break
            ret += len(T) - ti
        return ret
    left, right = -(10**18)-1, 10**18+1
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if count(mid) < K:
            left = mid
        else:
            right = mid
    return right

def solve(S, mS, K):
    def count(x, T):
        ret, j = 0, len(T) - 1
        for i, t in enumerate(T):
            while j >= 0 and t * T[j] > x:
                j -= 1
            if j == -1:
                break
            ret += j + 1 - (1 if i <= j else 0)
        return ret // 2
    left, right = -(10**18)-1, 10**18+1
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if count(mid, S) + count(mid, mS) < K:
            left = mid
        else:
            right = mid
    return right

def main():
    N, K = list(map(int, input().split()))
    A = sorted(map(int, input().split()), reverse=True)
    B = {-1:[], 0:[], 1:[]}
    for a in A:
        if a == 0:
            B[0].append(0)
        else:
            B[a//abs(a)].append(a)
    m = len(B[-1]) * len(B[1])
    z = len(B[0]) * (N-len(B[0])) + len(B[0]) * (len(B[0])-1) // 2
    if K <= m:
        print(solve_m(B[1], B[-1], K))
    elif K <= m + z:
        print(0)
    else:
        print(solve(sorted(B[1]), B[-1], K - m - z))


if __name__ == '__main__':
    main()
