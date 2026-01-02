# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

def io_generator():
	return input()

#+++++++++++++++++++

def isBitOn(value, n):
	return (value & (2 ** n)) > 0
	
def isMake(l,v):
	if len(l)==0 and v ==0:
		return True
		
	for i in range(2 ** len(l)):
		r=sum([v * (1-2*isBitOn(i,j)) for j,v in enumerate(l)])
		if r == v:
			return True
	return False
	
def move_next(v,i):
	rv = (v | 2 ** (i))
	ri = i+1
	return rv, ri
	
def buck(v,i):
	#111,3->101,3
	#101,3->010,2
	for j in range(i-1):
		n=i-1-j
		d=(v & 2** (n - 1))
		if d > 0:
			nv=(v & (2**(n-1) - 1))
			nnv,ni = move_next(nv, n)
			return True,nnv,ni
	return False, -1, -1
	
def isMake3(l,a_target):
	tree=0
	ii=0
	l.sort(reverse = True)
	est=lambda al,av:sum([v * isBitOn(av,j) for j,v in enumerate(l)])
	cc=True
	
	while cc:
		ccv=est(l, tree)
		#print(bin(tree),ii, est(l,tree),a_target)
		while ccv < a_target:
			tree, ii = move_next(tree,ii)
			#print(bin(tree),ii, est(l,tree),a_target)
			if ii > len(l):
				return False, -1
			ccv += l[ii-1]
			
		if ccv == a_target:
			return True, tree
		else:
			cc,tree,ii=buck(tree, ii)
			
	return False, -1
	
def isMake2(l, a_target):
	off=sum(l)
	if abs(a_target) > off:
		return False
	elif abs(a_target) == off:
		return True
	
	ll=[2*i for i in l]
	ret, _ = isMake3(ll, off + a_target)
	return ret
	
def isMakeDp(l, a_target):
	ss=set()
	ss.add(0)
	for v in l:
		next_ss=set()
		for p in list(ss):
			next_ss.add(p+v)
			next_ss.add(p-v)
		ss=next_ss
	return a_target in ss
		

def next(a_xy):
	return (a_xy+1)%2
	
def main(io):
	ft=io()
	goal = list(map(int, io().split()))
	
	isFirstMove=True
	init_pos=[0,0]
	xy=0
	mm=0
	ml=[[],[]]
	for c in ft:
		if isFirstMove and c=='F':
			init_pos[0]+=1
		elif isFirstMove and c=='T':
			isFirstMove=False
			xy = next(xy)
			mm=0
		elif c == 'F':
			mm+=1
		elif c== 'T':
			if mm > 0:
				ml[xy].append(mm)
			xy=next(xy)
			mm=0
	if mm>0:
		ml[xy].append(mm)

	is_debug=False
	if is_debug:
		print(ml)
		print(init_pos)
		print(goal)
	for i in range(2):
		if not isMakeDp(ml[i], goal[i] - init_pos[i]):
			return 'No'
	return 'Yes'

#++++++++++++++++++++

if __name__ == "__main__":
	io= lambda : io_generator()
	print (main(io))