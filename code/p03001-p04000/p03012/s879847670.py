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
    W = ria()
    s = sum(W)
    ans = s
    t = 0
    for i in range(N):
        t += W[i]
        s -= W[i]
        ans = min(ans, abs(s - t))
    print(ans)


if __name__ == "__main__":
    main()
