# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

def io_generator():
	return input()

#+++++++++++++++++++

def ll2l(a_list):
	ret=[]
	for i, v in enumerate(a_list):
		if i == 0 or ret[-1][0] != v:
			ret.append([v,1])
		else: #if ret[-1][0] == v:
			ret[-1][1] += 1
	return ret
		

def main(io):
	a, b = map(int, io().split())
	end_pos=0
	ok='Possible'
	ng='Impossible'
	for i in range(a):
		l = list(io())[:b]
		rr=ll2l(l)
		#print(rr)
		if len(rr) == 0:
			return ng
		elif len(rr) >= 4:
			return ng
		elif len(rr)==1 and rr[0][0] == '.':
			return ng
		elif len(rr)==1:
			st=0
			end = rr[0][1]-1
		elif len(rr) == 2 and rr[0][0]=='.':
			st = rr[0][1]
			end = st + rr[1][1]-1
		elif len(rr) == 2 and rr[0][0]=='#':
			st = 0
			end = rr[0][1] - 1
		elif len(rr) == 3 and rr[0][0]=='#':
			return ng
		else:
			st=rr[0][1]
			end=st + rr[1][1]-1
		#print(st,end)
		if end_pos != st:
			return ng
		end_pos = end
		
	if end_pos==b-1:
		return ok
	return ng
	
#++++++++++++++++++++

if __name__ == "__main__":
	io= lambda : io_generator()
	print (main(io))