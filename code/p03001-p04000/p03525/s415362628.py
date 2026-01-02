import sys

#+++++

def dd_max(ring):
	mm=25
	s=1
	for r in ring[1:]:
		#print(s,r,mm)
		if r >= 1:
			mm=min(s,mm)
			s=1
		else:
			s+=1
	return mm
	
		
def main():
	n = int(input())
	dl = list(map(int, input().split()))
	dl.append(0)
	
	#0が2個あったら0
	if dl.count(0) >=2:
		return 0
	#12が2個あったら0
	if dl.count(12) >=2:
		return 0
	#1-11が3個以上あったら0
	for i in range(1,11+1):
		if dl.count(i) >= 3:
			return 0
	
	ll=[0]*25
	ll[0]=1
	ll[24]=1
	cc=[]
	if dl.count(12) == 1:
		ll[12]=1
	for i in range(1,11+1):
		if dl.count(i)==2:
			ll[i]=1
			ll[24-i]=1
		if dl.count(i)==1:
			cc.append(i)
			
	if len(cc)==0:
		print(dd_max(ll))
		#print(ll)
		return 
	
	#1-11が2個あったらプラスとマイナスに配置が必須
	ret=0
	n_cc=len(cc)
	cc_max=(2**n_cc)-1
	for i in range(cc_max):
		tll=ll.copy()
		for j,v in enumerate(cc):
			if i & (2**j) > 0:
				tll[24-v]=1
			else:
				tll[v]=1
				
		tr=dd_max(tll)
		ret=max(ret, tr)
	
	print(ret)
	
	
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