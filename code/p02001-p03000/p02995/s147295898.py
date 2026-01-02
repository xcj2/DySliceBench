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
import random
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

def main():

	#S = int(input())
	#S = list(input())
	A,B,C,D = map(int, input().split(" "))
	#L = list(map(int, input().split(" ")))

	E = lcm(C, D)
	if A == B:
		if A % C == 0 or A % D == 0:
			print(0)
			sys.exit()
		else:
			print(1)
			sys.exit()

	if C == D or C % D == 0 or D % C == 0:
		tmp_C2 = B // C
		tmp_C2ama = B % C

		tmp_C1 = A // C
		tmp_C1ama = A % C

		tmp = (tmp_C2-tmp_C1)

		tmp2 = 0
		if tmp_C1ama == 0:
			tmp2 -=1

		ans = B-A-tmp+1+tmp2
		print(ans)
		sys.exit()

	tmp_C2 = B // C
	tmp_C2ama = B % C
	tmp_D2 = B // D
	tmp_D2ama = B % D
	tmp_C1 = A // C
	tmp_C1ama = A % C
	tmp_D1 = A // D
	tmp_D1ama = A % D

	tmp_E2 = B // E
	tmp_E2ama = B % E
	tmp_E1 = A // E
	tmp_E1ama = A % E

	tmp = (tmp_C2+tmp_D2)-(tmp_C1+tmp_D1)

	tmp2 = 0
	if tmp_C1ama == 0:
		tmp2 -=1
	if tmp_D1ama == 0:
		tmp2 -=1
	if tmp_E1ama == 0:
		tmp2 += 1

	#print(E)

	ans = B-A-tmp+1+(tmp_E2-tmp_E1)+tmp2

	print(ans)

def gcd(a, b):
	if a > b:
		a, b = b, a
		
	while a > 0:
		a, b = b % a, a
	return b

def lcm(a, b):
	g = gcd(a, b)
	return a // g * b

if __name__ == "__main__":
	main()