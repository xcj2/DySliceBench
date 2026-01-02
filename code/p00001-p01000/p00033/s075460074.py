# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**6)

def dfs(balls,B=-1,C=-2,cp=0):
	if cp==len(balls): 	return True
	ball = balls[cp]
	if B<ball:
		is_find = dfs(balls,ball,C,cp+1)
		if is_find: return True
	if C<ball:
		is_find = dfs(balls,B,ball,cp+1)
		if is_find: return True
	return False

def not_dfs(balls):
	B, C = -2, -1
	for ball in balls:
		if C<ball:
			C = ball
			continue
		if B<ball:
			B = ball
			continue
		return False
	return True

def main():
	N = int(input().strip())
	for _ in range(N):
		balls = list(map(int,input().split(' ')))
#		is_find = dfs(balls)
		is_find = not_dfs(balls)
		if is_find:		print('YES')
		else:			print('NO')

if __name__=='__main__':
	main()

"""
2
3 1 4 2 5 6 7 8 9 10
10 9 8 7 6 5 4 3 2 1
"""