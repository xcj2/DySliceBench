import sys
import math
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]


    
    
def main():
    N, M = MI()
    mylist = [[] for i in range(N)]
    for i in range(M):
        a, b = MI()
        mylist[a-1].append(b-1)
        mylist[b-1].append(a-1)
    
    dic = defaultdict(int)
    
    visit = [True]*N
    index = 0

    for i in range(N):
        dq = deque()
        if visit[i]:
            dq.append(i)
            while dq:
                temp = dq.popleft()
                for j in mylist[temp]:
                    if visit[j]:
                        dic[index]+=1
                        visit[j] = False
                        dq.append(j)
            index+=1
                
        
        
        
    #グループ数
    all_group_num = sorted(dic.values())
    res = 0
    all_num = N
    min_num = 0
    
    if sum(all_group_num) < N:
        all_group_num = [1]*(N-sum(all_group_num))+all_group_num
    group = len(all_group_num)

    while True:
        index = bisect_right(all_group_num, min_num)
        all_num -= (group-index)*(all_group_num[index]-min_num)
        res+= all_group_num[index]-min_num
        
        min_num = all_group_num[index]
        
        if all_num == 0:
            break
        
    print(res)

    
    
    
    
if __name__ == "__main__":
    main()