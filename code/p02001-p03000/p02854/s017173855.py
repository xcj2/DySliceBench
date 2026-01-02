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
	A = inputList()

	to = 0
	for i in A:
		to += i

	to = to // 2
	manaka = 0
	tmp = 0
	for i,val in enumerate(A):
		tmp += val
		if tmp >= to:
			manaka = i
			break

	#print(to)
	#print(manaka)

	to1 = 0
	to11 = 0
	to2 = 0
	to22 = 0

	to111 = 0
	to222 = 0

	for i,val in enumerate(A):
		if i >= manaka+1:
			to2 += val
		else:
			to1 += val

		if i >= manaka-1:
			to22 += val
		else:
			to11 += val

		if i >= manaka:
			to222 += val
		else:
			to111 += val

	ans = min(abs(to1-to2),abs(to11-to22),abs(to111-to222))
	print(ans)


if __name__ == "__main__":
	main()
