from sys import stdin
import sys
import numpy as np
import collections

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
    S = rs()
    K = ri()
    N = len(S)
    key = []
    cnt = []
    key.append(S[0])
    cnt.append(1)
    for i in range(1,N):
        if S[i] == key[len(key) - 1]:
            cnt[len(cnt) - 1] += 1
        else:
            key.append(S[i])
            cnt.append(1)

    if len(cnt) == 1:
        tot = N * K
        print(tot // 2)
        sys.exit(0)

    ans = 0
    for i in range(1,len(cnt) - 1):
        ans += K * (cnt[i] // 2)
    ans += cnt[0] // 2
    ans += cnt[len(cnt) - 1] // 2
    if(key[0] == key[len(key) - 1]):
        ans += (K - 1) * ((cnt[0] + cnt[len(cnt)-1]) // 2)
    else:
        ans += (K - 1) * ((cnt[0]) // 2)
        ans += (K - 1) * ((cnt[len(cnt)-1]) // 2)
    print(ans)






if __name__ == "__main__":
    main()
