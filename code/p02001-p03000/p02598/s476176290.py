import math
import sys
input = sys.stdin.readline
INF = float("inf")


def isOK(m, K, arr):
    cnt = 0
    for a in arr:
        if a > m:
            cnt += a // m
    return cnt <= K


def binary_search(ok, ng, K, arr=[]):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid, K, arr):
            ok = mid
        else:
            ng = mid
    return ok


# 処理内容
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    ok = 10**9
    ng = 0
    ans = binary_search(ok, ng, K, A)
    print(ans)


if __name__ == '__main__':
    main()