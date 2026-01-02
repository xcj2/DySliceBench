#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    S = input()
    N  = len(S)
    
    for i in range(N):
        if S[i] != S[N-i-1]:
            print("No")
            exit()
    half = int((N-1)/2)
    for i in range(half):
        if S[i] != S[half-i-1]:
            print("No")
            exit()
            
    for i in range(half+2,N):
        if S[i] != S[N-i-1]:
            print("No")
            exit()
        
    print("Yes")
    


main()
