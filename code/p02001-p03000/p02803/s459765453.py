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
	global Y
	global X
	global q
	global maps
	global maze

	H,W = inputMap()
	Y = H
	X = W
	mapmap = []
	ser = []
	for i in range(H):
		tmp = input()
		tmp = tmp[:-1]
		mapmap.append(tmp)

		for j,val in enumerate(tmp):
			if val == ".":
				ser.append((i,j))

	maps = [[-1 for _ in range(X)] for _ in range(Y)]
	maze = mapmap
	q = Queue()

	ans = 0
	for i,val in enumerate(ser):
		s,e = val
		tmp = serchs(s,e,s,e)

		for i in maps:
			tmptmp = max(i)
			#print(tmptmp)
			if tmptmp > ans:
				ans = tmptmp

		maps = [[-1 for _ in range(X)] for _ in range(Y)]

	print(ans)

def serchs(start_y,start_x, goal_y,goal_x):
	q.enqueue((start_y, start_x))
	maps[start_y][start_x] = 0
	run()

	return(maps[goal_y][goal_x])

def run():
	while True:
		tmp = q.dequeue()
		if tmp == None:
			return

		y, x = tmp

		counts = maps[y][x] + 1
		if not y <= 0 and maps[y-1][x] == -1 and maze[y-1][x] == ".":
			q.enqueue((y-1, x))
			maps[y-1][x] = counts
		if not x <= 0 and maps[y][x-1] == -1 and maze[y][x-1] == ".":
			q.enqueue((y, x-1))
			maps[y][x-1] = counts
		if not y >= Y-1 and maps[y+1][x] == -1 and maze[y+1][x] == ".":
			q.enqueue((y+1, x))
			maps[y+1][x] = counts
		if not x >= X-1 and maps[y][x+1] == -1 and maze[y][x+1] == ".":
			q.enqueue((y, x+1))
			maps[y][x+1] = counts

class Queue:
    def __init__(self, queue = None):
        if type(queue) is type([]):
            self.queue = queue
        else:
            self.queue = []

    def enqueue(self, e):
        self.queue.append(e)
        return self.queue

    def dequeue(self):
        try:
            qEl = self.queue[0]
            del self.queue[0]
            return qEl
        except IndexError:
            return None


if __name__ == "__main__":
	main()
