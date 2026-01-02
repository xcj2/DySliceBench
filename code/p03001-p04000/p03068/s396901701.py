from sys import stdin
import sys
##  input functions for me
def ria(sep = ''):
    if sep == '' :
        return list(map(int, input().split())) 
    else: return list(map(int, input().split(sep)))
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##
def main():
    N = ri()
    S = rs()
    K = ri() - 1
    ans = []
    for i in range(N):
        if S[i] != S[K]:
            ans.append('*')
        else:
            ans.append(S[K])
    print(''.join(ans))


if __name__ == "__main__":
    main()
