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

from decimal import *

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

##### 累乗 #####
# pow(x, y, z) -> x**y % z

def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))

inf = float('inf')
mod = 1000000007

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

def main():
	a,b,c = inputMap()
	getcontext().prec = 20007

	if Decimal(Decimal(a).sqrt() + Decimal(b).sqrt()) < Decimal(c).sqrt():
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
