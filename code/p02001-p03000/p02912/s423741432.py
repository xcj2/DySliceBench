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
	A = inputList()

	if len(A) == 1:
		print(A[0] // (2**M))
		sys.exit()

	A.sort()
	A = A[::-1]
	ans = 0
	A_new = []
	mimi = -1

	for i in range(1000000000000):
		for i,val in enumerate(A):
			if i == len(A)-1:
				A_new.append(val)
				break

			if mimi < val and M > 0:
				flg = False
				for j in range(1,M+1):
					if M - j != 0:
						tmp = val // (2**j)
						if tmp < A[i+1] or tmp < mimi:
							M -= j
							A_new.append(tmp)
							flg = True
							if mimi == -1:
								mimi = tmp
							break

				if flg == False:
					tmp = val // (2**M)
					M = 0
					A_new.append(tmp)

			else:
				A_new.append(val)

		#print(A_new)
		#A = copy.deepcopy(A_new)
		A = A_new
		A.sort()
		A = A[::-1]
		A_new = []
		mimi = -1

		if M == 0:
			break

	#print(A)

	ans = 0
	for i in A:
		ans += i

	print(ans)


if __name__ == "__main__":
	main()
