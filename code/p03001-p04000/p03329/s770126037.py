import sys

#+++++

def nn(val, count, aal):
	#pa((val,count,aal))
	if aal[val] >= 0:
		return aal[val]
	
	ll=[1]
	i=1
	while 6**i <= val:
		ll.append(6**i)
		i+=1
	
	i=1
	while 9 ** i <= val:
		ll.append(9**i)
		i+=1
	
	ll=ll[::-1]
	min_v = val
	for l in ll:
		temp = nn(val-l, count+1,aal)
		min_v = min(min_v,temp)
	
	aal[val]=min_v+1
	return min_v+1
	
	
		
def main():
	N = int(input())
	al=[-1]*(N+1)
	al[0:6]=[0,1,2,3,4,5]
	#print(al[0:10])
	ans=nn(N,0,al)

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