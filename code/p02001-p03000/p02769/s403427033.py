#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

# 逆元comb
def comb(n, k):
    k = min(n-k,k)
    ans = 1
    for i in range(1, k + 1):
        ans *= (n + 1 - i) * pow(i,MOD-2,MOD)
        ans %= MOD
        
    return ans

def solve(n: int, k: int):
    # nC0---n-1
    comb1 = [0]*n
    comb1[0] = 1
    for i in range(1, n):
        comb1[i] = (comb1[i-1]*(n + 1 - i) * pow(i,MOD-2,MOD))%MOD

    # nC0---n-1
    comb2 = [0]*(n-1)
    comb2[0] = 1
    for i in range(1, n-1):
        comb2[i] = (comb2[i-1]*(n - i) * pow(i,MOD-2,MOD))%MOD

    
    if k >= n-1: ## なんでもいける
        answer = 0
        for i in range(n): # i はゼロの数
            if i == 0:
                answer += 1
            else:
                answer += comb1[i]*comb2[n-1-i]%MOD
        print(answer%MOD)
        return
    else:
        answer = 0
        for i in range(k+1): # i はゼロの数
            if i == 0:
                answer += 1
            else:
                answer += comb1[i]*comb2[n-1-i]%MOD
        print(answer%MOD)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(n, k)

if __name__ == '__main__':
    main()
