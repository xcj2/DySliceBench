import sys
bbn=1000000007
	
#+++++

def mk_path(a_i, max_n, ret):
	#a_i = 1 ... max_n
	#7 => 7,(6,1),(5,2),(4,3)
	#8 => (8,1),(7,2),(6,3),(5,4)
	off=0 if max_n % 2 == 1 else 1
	
	for i in range(a_i+1, max_n+1):
		if i == max_n - a_i + off:
			continue
		else:
			ret.append((a_i, i))
			
	return 
	
def check_constraint(graph, n):
	cc=[0]*n
	for f,t in graph:
		cc[f-1] += t
		cc[t-1] += f
	
	pa(('max:',max(cc),', min:', min(cc) ))
	return
	
		
def main():
	n = int(input())
	ret=[]
	for i in range(1,n+1):
		mk_path(i,n,ret)
	
	#check_constraint(ret, n)
	print(len(ret))
	for f,t in ret:
		pass
		print(f,t)

	
	
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