import sys
bbn=1000000007
	
#+++++
		
def main2():
	n, k = map(int, input().split())
	sl = input()
	dd=[]
	ddv=[]
	left= sl[0]
	count=0
	pre=left
	for c in sl:
		if c == pre:
			count+=1
		else:
			dd.append(count)
			ddv.append(pre)
			pre=c
			count=1
	dd.append(count)
	ddv.append(pre)
	
	pa(ddv)
	if k == 0:
		return max([v for v,c in zip(dd,ddv) if c == '1'])
	
	ll=[]
	for i,c in zip(dd,ddv):
		if c == '0':
			pass
			
def main():
	n, k = map(int, input().split())
	sl = input()
	al=[]
	if sl[0]=='0':
		al.append(0)
	p=sl[0]
	count=1
	for c in sl[1:]:
		if c == p:
			count+=1
		else:
			al.append(count)
			count=1
			p=c
	else:
		al.append(count)
		if sl[-1]=='0':
			al.append(0)
			
	#pa(al)
	
	if 2*k+1 >= len(al):
		print(n)
		return 
	
	ret = al[0]
	for i in range(k):
		ret += al[2*i+1]
		ret += al[2*i+2]
	#pa(ret)
	rs=ret
	for i in range(k, (len(al)//2)):
		rs += al[2*i+1]
		rs += al[2*i+2]
		rs -= al[2*(i-k)+1]
		rs -= al[2*(i-k)]
		ret = max(rs, ret)
		#pa(rs)
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