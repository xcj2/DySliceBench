# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

def io_generator():
	return input()

def iil(a_io):
	return map(int, a_io().split())


#+++++++++++++++++++



def main(io):
	n,m =iil(io)
	aas=list(iil(io))
	bbs=[]
	for _ in range(m):
		b,c=iil(io)
		bbs.append((b,c))
		
	
	aas.sort()
	#print(aas)
	bbs=sorted(bbs, key=lambda t:-t[1])
	#print(bbs)
	bbii=0
	bbij=0
	ret=0
	ddd=0
	for i in aas:
		if ddd ==1:
			ret += i
			continue
			
		if i > bbs[bbii][1]:
			ret += i
			ddd=1
			continue
			
		ret += bbs[bbii][1]
		
		bbij+=1
		if bbij >= bbs[bbii][0]:
			bbij=0
			bbii+=1
		
		if bbii >= len(bbs):
			ddd=1
	return ret
			
			
		
	
	return

#++++++++++++++++++++

if __name__ == "__main__":
	io= lambda : io_generator()
	ret = main(io)
	if ret is not None:
		print(ret)