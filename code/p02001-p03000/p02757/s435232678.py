# coding: utf-8
# Your code here!

N, P = map(int, input().split())
S = list(map(int,list(input())))
U = [0 for i in range(N+1)]

d = 1
for i in range(N):
    U[N-(i+1)] = (U[N-i] + S[N-1-i] * d) % P
    d = 10 * d % P
    
def solve(U,S):
    if P == 2 or P == 5:
        return solve1(S)
    else:
        return solve2(U)
    
def solve1(S):
    ans = 0
    for i in range(N):
        if S[i] % P == 0:
            ans += i+1
    return ans

def solve2(U):
    ans = 0
    cnt = [0 for i in range(P)]
    for i in range(N+1):
        cnt[U[i]] += 1
    for i in range(P):
        p = cnt[i]
        ans += (p * (p-1)) // 2
    return ans

print(solve(U,S))