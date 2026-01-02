#import re
import sys
input = sys.stdin.readline
#import heapq
#import bisect
#from collections import deque
#import math

def main():
    n = input().strip()
    k = int(input())
    if k == 1:
        ans = k1(n)
    elif k == 2:
        ans = k2(n)
    elif k == 3:
        ans = k3(n)
    
    print(int(ans))


def k1(n):
    ans = 0
    return 9*(len(n)-1)+int(n[0])

def k2(n):
    ans = 0
    if len(n) == 1:
        ans = 0
    elif len(n) >= 2:
        ans += k1(str(int(n[1:])))
        ans += (int(n[0])-1)*9*(len(n)-1)
        ans += 9*9*(len(n)-1)*(len(n)-2)/2
    return ans

def k3(n):
    ans = 0
    if len(n) <= 2:
        ans = 0
    elif len(n) >= 3:
        ans += k2(str(int(n[1:])))
        ans += (int(n[0])-1)*9*9*(len(n)-1)*(len(n)-2)/2
        ans += (len(n)-1)*(len(n)-2)*(len(n)-3)/6*9**3
    return ans

    
if __name__ == '__main__':
    main()
