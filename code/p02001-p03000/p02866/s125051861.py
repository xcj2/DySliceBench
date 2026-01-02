# -*- coding: utf-8 -*-
import sys
import math
from bisect import bisect_left
from bisect import bisect_right
import collections
import copy
import heapq
from collections import defaultdict
from heapq import heappop, heappush
import itertools
input = sys.stdin.readline
 
##### リストの 二分木検索 #####
# bisect_left(lists, 3)
# bisect_right(lists, 3)
 
##### プライオリティキュー #####
# heapq.heapify(a) #リストaのheap化
# heapq.heappush(a,x) #heap化されたリストaに要素xを追加
# heapq.heappop(a) #heap化されたリストaから最小値を削除＆その最小値を出力
 
# heapq.heappush(a, -x) #最大値を取り出す時は、pushする時にマイナスにして入れよう
# heapq.heappop(a) * (-1) #取り出す時は、-1を掛けて取り出すこと
 
##### タプルリストのソート #####
# sorted(ans) #(a, b) -> 1st : aの昇順, 2nd : bの昇順
# sorted(SP, key=lambda x:(x[0],-x[1])) #(a, b) -> 1st : aの昇順, 2nd : bの降順
# sorted(SP, key=lambda x:(-x[0],x[1])) #(a, b) -> 1st : aの降順, 2nd : bの昇順
# sorted(SP, key=lambda x:(-x[0],-x[1])) #(a, b) -> 1st : aの降順, 2nd : bの降順
 
# sorted(SP, key=lambda x:(x[1])) #(a, b) -> 1st : bの昇順
# sorted(SP, key=lambda x:(-x[1])) #(a, b) -> 1st : bの降順
 
def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
 
def main():
    N = inputInt()
    D = inputList()
    
    if D[0] != 0:
        print(0)
        sys.exit()
        
    if N == 1:
        print(1)
        sys.exit()
        
    D.sort()
    
    if D[1] != 1:
        print(0)
        sys.exit()
        
    ck = 0
    dict_tmp = {}
    for i,val in enumerate(D):
        if ck == val:
            pass
        elif ck+1 == val:
            ck += 1
        else:
            print(0)
            sys.exit()
            
        if val in dict_tmp:
            dict_tmp[val] += 1
        else:
            dict_tmp[val] = 1
            
    ans = 1
    for k,v in dict_tmp.items():
        if k == 0 or k == 1:
            pass
        else:
            tmp = dict_tmp[k-1]
            for i in range(v):
                ans *= tmp
                ans = ans % 998244353
                
    print(ans)
            
    
    
if __name__ == "__main__":
	main()
