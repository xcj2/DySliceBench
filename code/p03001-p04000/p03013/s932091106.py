import sys
sys.setrecursionlimit(10**7)
import itertools


#debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    memo = {}

    def fib(n):
        if n in memo.keys():
            return memo[n]
        else:
            if n >= 4:
                ans = fib(n - 1) + fib(n - 2)
                memo[n] = ans
                return ans
            elif n == 3:
                return 2
            elif n == 2:
                return 1
            elif n == 1:
                return 1
            else:
                return 1

    n, m = map(int, input().split())
    w_list = []
    last = -1
    dead = False
    for i in range(m):
        a = int(input())
        w = a-last-1
        dprint(i, a, w)
        if w == 0:
            dead = True
            break
        w_list.append(w)
        last = a

    w_list.append((n+1)-last-1)

    dprint(w_list)

    mx = 10**9 + 7
    if dead == True:
        ans = 0
    else:
        ans = 1
        for w in w_list:
            fibw = fib(w)
            ans *= fibw
            dprint(w, fibw, ans)
            ans %= mx

    print(ans)

solve()