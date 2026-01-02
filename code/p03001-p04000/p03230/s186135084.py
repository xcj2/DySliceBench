#!/usr/bin/env python3
import sys
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    N =INT()
    size = 0
    for i in range(1,10**3):
        if i*(i+1)//2 == N:
            size = i 
            break
    else:
        print("No")
        return
    
    k = size + 1
    answer = [[] for _ in range(k)]

    start = 1
    for i in range(k):
        answer[i] = list(range(start,start+size-i))
        start += size-i
    
    for i in range(k-1):
        for j in range(i+1,k):
            answer[j].append(answer[i][j-i-1])
    
    print("Yes")
    print(k)
    for i in range(k):
        print(size,*answer[i])
    return

if __name__ == '__main__':
    main()
