#!/usr/bin/env python3
import sys
# input = sys.stdin.r/eadline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    N,C,K = MAP()
    T = [INT() for _ in range(N)]
    T.sort()
    passengers = 1
    deadline = T[0]+K
    answer = 0

    for i in range(1,N):
        if passengers<C and T[i]<=deadline:
            passengers += 1
        elif passengers == C or T[i]>deadline: #出発させる
            passengers = 1
            answer += 1
            deadline = T[i]+K
    if passengers>0:
        answer += 1
    print(answer)

if __name__ == '__main__':
    main()
