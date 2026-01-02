# -*- coding: utf-8 -*-

def io_generator():
	return input()

#+++++++++++++++++++

def t_search(a_list, pos):
	oo=10**20
	if pos< a_list[0]:
		pm=oo
		pp=a_list[0]-pos
		return pm,pp
	elif pos>a_list[-1]:
		pm=pos-a_list[-1]
		pp=oo
		return pm,pp
	ok=0
	ng=len(a_list)-1
	while abs(ok-ng)>1:
		mid=(ok+ng)//2
		if a_list[mid]<=pos:
			ok=mid
		else:
			ng=mid
	
	if a_list[ok]==pos:
		return 0,0
	pm=a_list[ok]
	pp=a_list[ok+1]
	return pos-pm, pp-pos

def main(io):
	a,b,q= map(int, io().split())
	syu=list(range(a))
	ten=list(range(b))
	for i in range(a):
		syu[i]=int(io())
	for i in range(b):
		ten[i]=int(io())
		
	ret=list(range(q))
	for i in range(q):
		init_pos=int(io())
		md_syu,pd_syu = t_search(syu,init_pos)
		md_ten,pd_ten= t_search(ten,init_pos)
		r=min(
			max(md_syu,md_ten),
			md_syu*2+pd_ten,
			pd_syu*2+md_ten,
			md_ten*2+pd_syu,
			pd_ten*2+md_syu,
			max(pd_syu,pd_ten)
			)
		ret[i]=str(r)
		
	for r in ret:
		print(r)

#++++++++++++++++++++

if __name__ == "__main__":
	io= lambda : io_generator()
	main(io)