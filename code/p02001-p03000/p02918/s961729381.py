import sys
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, K = MAP()
S = input()

def searchRL(S):
    ans = []
    for i in range(N-1):
        if S[i] == "R" and S[i+1] == "L":
            ans.append(i)
    return ans

def searchLR(S):
    ans = []
    for i in range(N-1):
        if S[i] == "L" and S[i+1] == "R":
            ans.append(i)
    return ans

def reverse(S):
    S = list(S)
    for i in range(len(S)):
        if S[i] == 'L':
            S[i] = 'R'
        if S[i] == 'R':
            S[i] = 'L'
    return ''.join(S)


def solve(S):
    if len(RL) == 0 and len(LR) == 0:
        return S, 0
    if len(RL) == 0:
        S = reverse(S[LR[0]::-1]) + S[LR[0]+1:]
        LR.pop(0)
        return S, 1
    if len(LR) == 0:
        S = reverse(S[RL[0]::-1]) + S[RL[0]+1:]
        RL.pop(0)
        return S, 1
    fir = min(LR[0], RL[0])
    sec = max(LR[0], RL[0])
    S = S[:fir+1] + reverse(S[sec:fir:-1]) + S[sec+1:]
    LR.pop(0)
    RL.pop(0)
    return S, 2

def cal(S):
    ans = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            ans +=1
    return ans

RL = searchRL(S)
LR = searchLR(S)
ans = cal(S)
for i in range(K):
    S, res = solve(S)
    ans += res
print(ans)
