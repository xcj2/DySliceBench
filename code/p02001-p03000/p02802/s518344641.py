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
	N,M = inputMap()
	ansrs_AC = [0 for i in range(N)]
	ansrs_WA = [0 for i in range(N)]
	ans1 = 0
	ans2 = 0
	for i in range(M):
		inp = input()
		inp = inp[:-1]
		p, S = inp.split(" ")
		pp = int(p)
		if S == "AC":
			if ansrs_AC[pp-1] == 1:
				continue
			else:
				ansrs_AC[pp-1] = 1
		else:
			if ansrs_AC[pp-1] == 1:
				continue
			else:
				ansrs_WA[pp-1] += 1

	for i in range(N):
		if ansrs_AC[i] == 1:
			ans1 += 1
			ans2 += ansrs_WA[i]
	print("{} {}".format(ans1, ans2))

if __name__ == "__main__":
	main()
