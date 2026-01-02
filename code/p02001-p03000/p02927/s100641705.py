def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors
def examA():
    M, D = LI()
    c = D//10
    ans = 0
    for i in range(2,M+1):
        d = make_divisors(i)
#        print(d)
        for j in range(len(d)//2):
            cur0 = d[j*2+1]; cur10 = d[j*2]
            if cur10==1:
                continue
            if cur0<=9:
                if cur10<c:
                    ans +=1
#                    print(cur10,cur0)
                elif cur10==c and cur0+cur10*10<=D:
                    ans +=1
#                    print(cur10,cur0)
        for j in range(len(d) // 2):
            cur0 = d[j * 2];cur10 = d[j * 2+1]
            if cur0 == 1:
                continue
            if cur10 <= 9:
                if cur10 < c:
                    ans += 1
                elif cur10 == c and cur0 + cur10 * 10 <= D:
                    ans += 1
        if len(d)%2==1:
            cur0 = d[-1]; cur10 = d[-1]
            if cur10==1:
                continue
            if cur0<=9:
                if cur10<c:
                    ans +=1
#                    print(cur10,cur0)
                elif cur10==c and cur0+cur10*10<=D:
                    ans +=1
#                    print(cur10,cur0)
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,inf
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examA()
