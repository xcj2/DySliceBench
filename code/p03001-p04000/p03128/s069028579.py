import sys
import queue

#+++++

def sa(v, p):
	return v //p, v %p

def ggg(value, p_list, ctv):
	dd=p_list[:]
	#print('gfg',dd)
	if len(dd)==0:
		return None
	a=dd.pop(0)
	if a > value:
		return None
	
	m,p=sa(value, a)
	if p == 0:
		aa= [max(ctv[a])]*(m)
		return aa
	else:
		best_st=None
		for i in range(min(m+1,6)):
			nokori=p+i*a
			ret=bbb(nokori, ctv)
			if ret is not None:
				aa= [max(ctv[a])]*(m-i)
				st=ret+aa
				if is_big(st, best_st):
					best_st=st
				
		return best_st

def bbb(value, ctv):
	ol=queue.PriorityQueue()
	kk_costs=ctv.keys()
	
	best_st=None
	
	cc=0
	st=[]
	ol.put((cc,(cc, st)))
	while not ol.empty():
		scc, (cc, st) = ol.get()
		#pa((scc,cc,st))
		if scc > value:
			return best_st
			
		if scc == value:
			if is_big(st, best_st):
				best_st=st
			continue
				
		for cost in kk_costs:
			tst=st[:]
			tst.append(max(ctv[cost]))
			ol.put((cc+cost, (cc+cost, tst)))
	return None
	
def is_big(base, other):
	if other is None:
		return True
	if base is None:
		return False
		
	if len(base) != len(other):
		return len(base) > len(other)
	return base > other


def mk_value(a_ll):
	if a_ll is None:
		return 0
		
	a_ll.sort(reverse=True)
	a_ll2=[str(v) for v in a_ll]
	ans=''.join(a_ll2)
	return ans
	
def main():
	n , _ = map(int, input().split())
	al = list(map(int, input().split())	)
	
	cost_list=[1000, 2,5,5,4,5,6,3,7,6]
	
	aal=[(v, cost_list[v]) for v in al]
	aal.sort(key=lambda x:-x[0])
	ctv={}
	for v in aal:
		ctv.setdefault(v[1], []).append(v[0])
	
	#for kk in ctv.keys():
	#	pa((kk,':',ctv[kk]))
	aal=list(ctv.keys())
	aal.sort()
	
	ccc = ggg(n, aal, ctv)
	ans=mk_value(ccc)
	
	print(ans)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)