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

def get_c(aa,ab,ac, amm):
	if ac < amm[2]-1:
		ret=[[aa,ab,ac+1]]
	else:
		ret=[]
		
	if ab<amm[1]-1:# and ab >= ac:
		ret.append([aa,ab+1,ac])
	
	if aa<amm[0]-1:# and aa >= ab and aa >= ac:
		ret.append([aa+1,ab,ac])
	return ret
	
def gv(al,bl,cl,s):
	return al[s[0]]+bl[s[1]]+cl[s[2]]
	
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
	init=[0,0,0]
	ggv=lambda l : gv(al,bl,cl,l)
	
	qq = []
	heappush(qq,Foo(ggv(init), init))
	
	ol=set()
	ol.add(lss(init))
	
	for _ in range(k):
		ff=heappop(qq)
		vv=ff.value
		cs=ff.state
		nc=get_c(cs[0],cs[1],cs[2],ml)
		print(vv)
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