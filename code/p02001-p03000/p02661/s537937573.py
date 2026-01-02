import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(IN())
mod=1000000007

#+++++

def is_median(k, xl, is_odd):
	over = 0
	under = 0
	inner = 0
	same = 0
	for a,b in xl:
		if b < k:
			under+=1
		elif k<a:
			over+=1
		elif a==k and b == k:
			same+=1
		else:
			inner+=1
	
	if abs(under-over) < same+inner:
		return 0
	else:
		return 1 if under > over else -1

def main2():
	n = int(input())
	#b , c = tin()
	xl=[]
	for _ in range(n):
		a,b = tin()
		xl.append((a,b))
	#s = input()
	min_v=0
	max_v=mod
	for a,b in xl:
		min_v=min(min_v, a)
		max_v=max(max_v, b)
	
	d = 1 if n % 2 == 0 else 1/2
	
	k_max_ok = min_v
	k_max_ng = max_v
	while k_max_ng - k_max_ok > d:
		pass
	
	k_min_ok = min_v
	
def main():
	n = int(input())
	al=[]
	bl=[]
	for i in range(n):
		a,b = tin()
		al.append(a)
		bl.append(b)
		
	al.sort()
	bl.sort()
	
	if n % 2 == 1:
		pos = ((n + 1) // 2) - 1
		d = bl[pos] - al[pos] + 1
		return d
	else:
		pos_l = ((n) // 2) - 1
		pos_r = pos_l + 1
		
		if al[pos_r] < bl[pos_l]:
			r = bl[pos_l] - al[pos_l] + bl[pos_r] - al[pos_r] + 1 - max(0, al[pos_r]-bl[pos_l])
		else:
			#return 1/0
			median_min = al[pos_l] + al[pos_r]
			median_max = bl[pos_l] + bl[pos_r]
			r = median_max - median_min + 1
			#pa((median_min,median_max))
		return r
		
			
		
	
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