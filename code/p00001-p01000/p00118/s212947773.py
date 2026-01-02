# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10000000)

def search(values,hp,vp,item):
	if not (0<=hp<len(values)): return
	if not (0<=vp<len(values[hp])): return
	if item!=values[hp][vp]: return
	values[hp][vp]=True
	search(values,hp-1,vp,item)
	search(values,hp+1,vp,item)
	search(values,hp,vp-1,item)
	search(values,hp,vp+1,item)

def solve(values):
	count,valid_items=0,set(['@','#','*'])
	for i in range(len(values)):
		for j in range(len(values[i])):
			if values[i][j] in valid_items:
				search(values,i,j,values[i][j])
				count+=1
	return count

def main():
	line,values=input().strip(),list()
	while line!='0 0':
		H,W = list(map(int,line.split(' ')))
		value = list()
		for _ in range(H):
			value.append(list(x for x in input().strip()))
		values.append(value)
		line = input().strip()
	for value in values:
		print(solve(value))

if __name__=='__main__':
	main()