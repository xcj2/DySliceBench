import sys
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#n,m = int(input())
	#b , c = tin()
	#s = input()	
	n, m = tin()
	
	ll=[[] for _ in range(n)]
	for _ in range(m):
		a, b = tin()
		ll[a-1].append(b-1)
		ll[b-1].append(a-1)
		
	gid=-1
	gg=[-1]*n
	for i in range(n):
		if gg[i] != -1:
			continue
		gid += 1
		gg[i] = gid
		q=collections.deque()
		q.append(i)
		while q:
			p = q.popleft()
			for np in ll[p]:
				if gg[np] != -1:
					continue
				gg[np]=gid
				q.append(np)
				
	cc=collections.Counter(gg)
	ret=0
	for k in cc:
		ret = max(ret, cc[k])
	return ret
	
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)