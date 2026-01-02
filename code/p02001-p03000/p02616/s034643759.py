import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
import bisect
from functools import reduce

def main():
    mod = 10 ** 9 + 7
    N, K = MI()
    A = LI()
    flag = 0
    for a in A:
        if a >= 0:
            flag = 1
            break

    A.sort(key=lambda x: abs(x), reverse=True)

    if K == N:
        ans = 1
        for a in A:
            ans *= a
            ans %= mod
        print(ans % mod)
        exit()
    elif flag == 0 and K % 2 != 0:
        B = A[::-1]
        ans = 1
        for i in range(K):
            ans *= B[i]
            ans %= mod
        ans %= mod
        print(ans)
        exit()
    else:
        ans = 1
        now_p = 0
        now_n = 0
        cnt_n = 0
        for i in range(K):
            a = A[i]
            ans *= a
            ans %= mod
            if a > 0:
                now_p = a
            elif a < 0:
                now_n = a
                cnt_n += 1
            else:
                print(0)
                exit()
        if cnt_n % 2 == 0:
            print(ans)
            exit()
        else:
            next_p = 0
            next_n = 0
            flag_p = 0
            flag_n = 0
            for i in range(K, N):
                a = A[i]
                if a > 0 and flag_p == 0:
                    next_p = a
                    flag_p = 1
                elif a < 0 and flag_n == 0:
                    next_n = a
                    flag_n = 1
                if flag_n == 1 and flag_p == 1:
                    break
                if a == 0:
                    break
        if now_p == 0:
            ans *= (pow(now_n, mod - 2, mod) * next_p) % mod
            ans %= mod
        elif next_p != 0 and next_n != 0:
            if now_p * next_p <= now_n * next_n:
                ans *= (pow(now_p, mod - 2, mod) * next_n) % mod
                ans %= mod
            else:
                ans *= (pow(now_n, mod - 2, mod) * next_p) % mod
                ans %= mod
        elif next_p == 0:
            ans *= (pow(now_p, mod - 2, mod) * next_n) % mod
            ans %= mod
        elif next_n == 0:
            ans *= (pow(now_n, mod - 2, mod) * next_p) % mod
            ans %= mod


        print(ans)

if __name__ == "__main__":
    main()
