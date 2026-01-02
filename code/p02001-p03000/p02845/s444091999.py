#!/usr/bin/env python3
import sys
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    N = INT()
    A = LI()
    RGB = [0,0,0]
    answer = 1
    MOD = 10**9+7

    for i in range(N):
        if RGB.count(A[i]) == 0:
            print(0)
            return

        answer *= RGB.count(A[i])
        answer %= MOD
        for j in range(3):
            if RGB[j] == A[i]:
                RGB[j] += 1
                break

    print(answer)
    return

if __name__ == '__main__':
    main()
