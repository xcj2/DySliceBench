#!/usr/bin/env python3
import sys

a = [0, 2,5,5,4,5,6,3,7,6]

def sort_str(s):
    ret = list(s)
    ret.sort(reverse=True)
    return ''.join(ret)

def is_greater(a, b):
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False
    for i in range(len(a)):
        if a[i] > b[i]:
            return True
        else:
            return False
    return False

def _solve(n: int, m: int, A: "List[int]"):
    dp = [None] * (n + 1)
    dp[0] = ''
    for c in A:
        for i in range(n + 1):
            if i - a[c] >= 0 and dp[i - a[c]] is not None:
                tmp = sort_str(dp[i - a[c]] + str(c))
                if dp[i] is None or is_greater(tmp, dp[i]):
                    dp[i] = tmp
        #print(dp)
    print(dp[n])
    return

def solve(n: int, m: int, A: "List[int]"):
    dp = [-1] * (n + 1)
    memo = ['' for _ in range(n + 1)]
    dp[0] = 0
    A.sort(reverse=True)
    #A.sort()
    for c in A:
        for i in range(n + 1):
            if i - a[c] >= 0 and dp[i - a[c]] >= 0:
                dp[i] = max(dp[i], dp[i - a[c]] * 10 + c)
                #if dp[i] < dp[i - a[c]] + 1:
                #    dp[i] = dp[i - a[c]] + 1
                #    memo[i] = memo[i - a[c]] + str(c)
        #print(dp)
        #print(memo)
    print(dp[n])
    #ret = list(memo[n])
    #ret.sort(reverse=True)
    #ret = ''.join(ret)
    #print(ret)
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(M) ]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
