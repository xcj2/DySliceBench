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
	#N,K = inputMap()
	HH = inputInt()
	ans = 0

	H = []
	sin = []
	H.append(HH)

	cnte = 1
	flg = False
	while True:
		#print(cnte)
		if cnte % 2 == 1:
			sin = []
			for i,val in enumerate(H):
				if val <= 1:
					ans += 2**(cnte-1)
					continue
				else:
					flg = True
					ans += 2**(cnte-1)
					sin.append(val//2)
					#sin.append(val//2)
			if flg == False:
				print(ans)
				sys.exit()
			else:
				flg = False

		else:
			H = []
			for i,val in enumerate(sin):
				if val <= 1:
					#print("ss")
					ans += 2**(cnte-1)
					continue
				else:
					flg = True
					ans += 2**(cnte-1)
					H.append(val//2)
					#H.append(val//2)
			if flg == False:
				print(ans)
				sys.exit()
			else:
				flg = False

		cnte += 1

	#print(ans)




if __name__ == "__main__":
	main()
