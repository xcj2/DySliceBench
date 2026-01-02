from sys import stdin
import sys
##  input functions for me
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def rip(sep = ''):
    if sep == '' :
        return map(int, input().split()) 
    else: return map(int, input().split(sep))
def ria(sep = ''): 
    return list(rip(sep))
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##
def main():
    N, M = rip()
    A = [ri() for i in range(M)]

    fbd = [False] * (N + 1)
    for n in A: fbd[n] = True
    dp = [0] * (N + 1)
    dp[0] = 1
    mod = int(1e9 + 7)
    for i in range(N):
        for j in range(1,3):
            if i + j <= N and not fbd[i + j]:
                dp[i + j] += dp[i]
                if dp[i + j] >= mod: dp[i + j] -= mod
    
    print(dp[N])
    

if __name__ == "__main__":
    main()
