#!/usr/bin/env python3
import sys
# input = sys.stdin.r/eadline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    N = INT()
    A = LI()

    last = A[0]
    is_increase = None
    answer = 0
    for i in range(1,N):
        if last == A[i]:
            continue
        if is_increase == None:
            is_increase = last<=A[i]
            last = A[i]
            continue

        if is_increase and last<=A[i]:
            last = A[i]
            continue
        
        if not is_increase and last>=A[i]:
            last = A[i]
            continue

        if (is_increase and last>A[i]) or (not is_increase and last<A[i]):
            is_increase = None
            last = A[i]
            answer += 1

    answer += 1
    print(answer)


if __name__ == '__main__':
    main()
