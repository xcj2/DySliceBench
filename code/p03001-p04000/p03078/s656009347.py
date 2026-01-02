# -*- coding: utf-8 -*-

from heapq import heappush, heappop
def io_generator():
	return input()

#+++++++++++++++++++
	
class Foo(object):
	def __init__(self, value, state):
		self.state = state
		self.value = value

	def __lt__(self, other):
		return self.value > other.value

def get_c(a_state, a_mm):
	ret=[]
	for i, _ in enumerate(a_state):
		if a_state[i] >= a_mm[i]-1:
			continue
		ret.append([v + (i==j) for j,v in enumerate(a_state)])

	return ret
	
def gv(a_l,a_state):
	ret= sum([l[s] for l, s in zip(a_l, a_state)])
	return ret
	
def lss(l):
	return '_'.join([str(i) for i in l])
	
def main(io):
	x,y,z,k=map(int, io().split())
	ml=[x,y,z]
	al =list(map(int, io().split()))
	al.sort(reverse=True)
	bl =list(map(int, io().split()))
	bl.sort(reverse=True)
	cl =list(map(int, io().split()))
	cl.sort(reverse=True)
	ls=[al,bl,cl]
	ggv=lambda l : gv(ls,l)
	
	qq = []
	ol=set()
	
	init=[0,0,0]
	heappush(qq,Foo(ggv(init), init))
	ol.add(lss(init))
	
	for _ in range(k):
		ff=heappop(qq)
		print(ff.value)
		cs=ff.state
		nc=get_c(cs,ml)
		for ns in nc:
			if lss(ns) in ol:
				continue
			else:
				heappush(qq, Foo(ggv(ns), ns))
				ol.add(lss(ns))
	return 1

#++++++++++++++++++++

if __name__ == "__main__":
	io= lambda : io_generator()
	#print (main(io))
	main(io)