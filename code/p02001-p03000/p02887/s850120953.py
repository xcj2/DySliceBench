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
    N = ri()
    S = rs()
    l = []
    l.append(S[0])
    for i in range(1,N):
        if S[i] != l[len(l) - 1]: l.append(S[i])
    print (len(l))


if __name__ == "__main__":
    main()
