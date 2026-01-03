import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def m_dist(p,q):
	return abs(p[0]-q[0])+abs(p[1]-q[1])

def gg(pos, ssl):
	mmm=m_dist(pos,ssl[0])
	m_id=0
	for i, q in enumerate(ssl[1:], 1):
		td=m_dist(pos, q)
		if td < mmm:
			mmm = td
			m_id = i
	return m_id
		
def main():
	#a = int(input())
	n, m = tin()
	#s = input()
	pl=[lin() for _ in range(n)]
	ssl = [lin() for _ in range(m)]
	for p in pl:
		r = gg(p, ssl)
		#pa((p,ssl))
		print(r+1)
	
	
	
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