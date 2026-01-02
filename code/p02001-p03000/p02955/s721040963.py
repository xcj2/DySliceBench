#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, K: int, A: "List[int]"):
    s = sum(A)
    A.sort()
    i = 1
    #print(s)
    #print(A)
    ret = 1
    def is_ok(n):
        downs = []
        for v in A:
            downs.append(v % n)
        downs.sort()
        #print(n, downs)
        cnt = float('inf')
        for i in range(1, N):
            left = 0
            right = 0
            for l in range(i):
                left += downs[l]
            for r in range(i, N):
                right += (n - downs[r])
            tmp = max(left, right)
            cnt = min(cnt, tmp)
            #print(i, left, right, cnt)
        #print(cnt)
        if cnt <= K:
            return True
        return False

    while i * i <= s:
        if s % i == 0:
            if is_ok(s // i):
                ret = max(ret, s // i)
            if is_ok(i):
                ret = max(ret, i)
        i += 1
    print(ret)
    return


def _solve(N: int, K: int, A: "List[int]"):
    s = sum(A)
    A.sort()
    i = 1
    print(s)
    print(A)
    ret = 1
    def is_ok(n):
        cnt = 0
        ls = 0
        us = 0
        bs = 0
        for v in A:
            tmp = v // n
            l = abs(v - n * (tmp))
            u = abs(v - n * (tmp + 1))
            if l < u:
                ls += l
            elif l > u:
                us += u
            else:
                bs += l
        cnt = max(ls, us)
        #cnt = min(ls, us)
        #rest = abs(ls - us)
        #if rest >= bs:
        #    rest -= bs
        #    cnt += bs + rest
        print(n, ls, us, cnt)
        if cnt <= K:
            return True
        return False

    while i * i <= s:
        if s % i == 0:
            if is_ok(s // i):
                ret = max(ret, s // i)
            if is_ok(i):
                ret = max(ret, i)
        i += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
