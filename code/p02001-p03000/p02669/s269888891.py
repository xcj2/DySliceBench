import sys

readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

from heapq import heappop, heappush

t = readint()

ans = []

for _ in range(t):
    n,a,b,c,d = readints()
    x = [0,0,a,b,0,c]
    h = [(0,n)]
    dct = dict()
    while 1:
        cost,num = heappop(h)
        if num == 1:
            break
        for i in (2,3,5):
            new_cost = cost + min(x[i]+(num%i)*d,(num-num//i)*d)
            new_num = num//i
            if new_num not in dct or new_cost<dct[new_num]:
                heappush(h,(new_cost,new_num))
                dct[new_num] = new_cost
            new_cost = cost + min(x[i]+(i-num%i)*d,(num-num//i-1)*d)
            new_num = num//i+1
            if new_num not in dct or new_cost<dct[new_num]:
                heappush(h,(new_cost,new_num))
                dct[new_num] = new_cost

    ans.append(cost+d)

printrows(ans)