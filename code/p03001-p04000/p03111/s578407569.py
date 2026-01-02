import sys
import queue

#+++++


def aaa(ll,a,b,c):
	ret=a+b+c
	for i,v1 in enumerate(ll):
		if v1==0:
			continue
		t1=abs(a-v1)
		if ret < t1:
			continue
		for j,v2 in enumerate(ll):
			if v2==0:
				continue
			if i==j:
				continue
			t2=t1 + abs(b-v2)
			if ret < t2:
				continue
			for k,v3 in enumerate(ll):
				if v3==0:
					continue
				if i==k or j==k:
					continue
				t3 = t2 + abs(c-v3)
				ret=min(ret, t3)
	return ret		

def mk_str(ll):
	ll.sort()
	return '_'.join([str(v) for v in ll])


def main():
	n , a, b, c = map(int, input().split())
	est=lambda ll:aaa(ll,a,b,c)
	
	bb=[]
	for i in range(n):
		bb.append(int(input()))
	
	cl=set()
	ol=queue.PriorityQueue()
	

	
	st=bb
	ee=est(st)
	cc=0
	cl.add(mk_str(bb))
	ol.put((ee+cc, (cc, bb)))	
	while True:
		if ee == 0:
			return cc
		
		#to goal no join
		rr=cc+ee
		ol.put((rr, (rr, [a,b,c])))
		
		
		
		#join 1
		if len(st) > 3:
			cc+=10
			for i, v in enumerate(st):
				kk=st[:]
				m=kk.pop(i)
				for j, _ in enumerate(kk):
					kkk=kk[:]
					kkk[j]+=m
					stk=mk_str(kkk)
					if stk not in cl:
						cl.add(stk)
						ol.put((cc, (cc, kkk)))
		v,(cc, st) = ol.get()
		ee = est(st)
				
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