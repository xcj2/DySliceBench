# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**6)

def search(field,hp,vp,item):
	if not (0<=hp<len(field)): return
	if not (0<=vp<len(field[hp])): return
	if item!=field[hp][vp]: return
	field[hp][vp]=True
	for dh,dv in [[0,1],[0,-1],[1,0],[-1,0]]:
		search(field,hp+dh,vp+dv,item)
#	search(field,hp-1,vp,item)
#	search(field,hp+1,vp,item)
#	search(field,hp,vp-1,item)
#	search(field,hp,vp+1,item)

def solve(field):
	count,valid_items=0,set(['@','#','*'])
	for i in range(len(field)):
		for j in range(len(field[i])):
			if field[i][j] in valid_items:
				search(field,i,j,field[i][j])
				count+=1
	return count

def main():
	line = input().strip()
	while line!='0 0':
		H,W = list(map(int,line.split(' ')))
		field = list()
		for _ in range(H):
			field.append(list(input().strip()))
		print(solve(field))
		line = input().strip()

if __name__=='__main__':
	main()