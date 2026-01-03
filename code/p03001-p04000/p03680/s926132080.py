#!/usr/bin/env python3
import sys
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    N = INT()
    Button = [INT() for _ in range(N)]

    count = 0
    isVisited = [False]*N
    GOAL = 1

    cur = 0
    while True:
        next = Button[cur]-1
        count += 1

        if next == GOAL:
            print(count)
            return
        
        if isVisited[next]:
            print(-1)
            return
        isVisited[next] = True
        cur = next
        
    return

if __name__ == '__main__':
    main()
