#!/usr/bin/env python3
import sys
# input = sys.stdin.r/eadline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    A,B,C = MAP()
    if A==B==C:
        if A%2==1 or B%2==1 or C%2==1:
            print(0)
        else:
            print(-1)
        return
    answer = 0
    
    while A%2==0 and B%2==0 and C%2==0:
        x = A//2
        y = B//2
        z = C//2
        A = y+z
        B = x+z
        C = y+x
        answer += 1
    print(answer)

if __name__ == '__main__':
    main()
