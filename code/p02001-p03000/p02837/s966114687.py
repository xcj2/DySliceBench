import sys
bbn=1000000007
	
#+++++

def get_m(says, state, person):
	if person == len(state):
		return sum(state)
	
	if state[person] == 0:
		return get_m(says,state,person+1)
		
	if state[person]==1:
		sss=state[:]
		for x,y in says[person]:
			if sss[x] == -1:
				sss[x]=y
			elif sss[x] != y:
				#mujun
				return 0
			else:
				continue
			
		return get_m(says,sss,person+1)
		
	
	sa=state[:]
	sa[person]=0
	a = get_m(says, sa, person+1)
	
	sb=state[:]
	sb[person]=1
	for x,y in says[person]:
		if sb[x] == -1:
			sb[x]=y
			
		elif sb[x] != y:
			#mujun
			return a
		else:
			continue
		
	b=get_m(says,sb,person+1)
	
	return max(a, b)
		
def main():
	n = int(input())
	says = [[] for _ in range(n)]
	for i in range(n):
		aij=int(input())
		for j in range(aij):
			x,y=map(int, input().split())
			says[i].append([x-1,y])
			
	a=[-1]*n
	
	ret=get_m(says, a,-1)
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