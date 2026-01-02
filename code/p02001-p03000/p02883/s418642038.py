import sys
import queue
bbn=1000000007
	
#+++++

def can_finish(time, a_c_qq, a_k):
	kc=a_k
	
	#if time==12:
	#	print(*a_c_qq)
		
	for (st,a,f) in (a_c_qq):
		if st <= time:
			return True
		
		#time => f*a' を目指す。
		#a' <= time / f が必要。
		#コストは a - (time // f)
		kc -= a - (time//f)
		#if time==12:
		#	pa((st,a,f, time,(time//f),a- (time//f),kc))
		
		if kc < 0:
			return False
		
	return True
	
		
def main():
	n, k = map(int, input().split())
	al=list(map(int, input().split()))
	fl=list(map(int, input().split()))
	
	qq=queue.PriorityQueue()
	
	al.sort(reverse=True)
	fl.sort()
	qq=[(a*f,a,f) for a,f in zip(al,fl)]
	qq.sort(reverse=True)

	#while not qq.empty():
	#	a=qq.get()
	#	pa(a)
	
	ok_max,_,_=qq[0]
	if sum(al) <= k:
		return 0
	ng_min=0
	
	while ok_max - ng_min > 1:
		mid = (ok_max + ng_min)// 2
		can_do = can_finish(mid, qq, k)
		#pa((ok_max,ng_min,mid,can_do))
		if can_do:
			ok_max = mid
		else:
			ng_min = mid

	print(ok_max)
	
	
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