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

##### 無限 #####
# inf = float('inf')

def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))

inf = float('inf')

def main():
	S = input()
	S = S[:-1]
	N = len(S)

	K = inputInt()

	dp = [[[0 for ii in range(2)] for j in range(K+1)] for i in range(N+1)]
	dp[0][0][0] = 1

	cnt = 1
	for i in range(N):
		for j in range(K+1):
			for k in range(2):
				targetN = int(S[i])
				for num in range(10):
					ni = i+1
					nj = j
					nk = k

					if num != 0:
						nj += 1
						if nj > K:
							continue

					if k == 0:
						if num > targetN:
							continue
						elif num == targetN:
							nk = 0
						else:
							nk = 1
					else:
						nk = 1

					dp[ni][nj][nk] += dp[i][j][k]
		cnt += 1

	print(dp[N][K][0] + dp[N][K][1])

if __name__ == "__main__":
	main()
