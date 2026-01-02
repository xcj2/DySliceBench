#!/usr/bin/env python3
import sys

def check(x, lst, k):
    cnt = 0
    for l in lst:
        cnt += (l - 1) // x
    if cnt  <= k:
        return True
    else:
        return False
    

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    def check(x):
        cnt = 0
        for l in a:
            cnt += (l - 1) // x
        if cnt  <= k:
            return True
        else:
            return False
    
    ng = 0
    ok = 10 ** 9
    
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    
    print(ok)


if __name__ == '__main__':
    main()
