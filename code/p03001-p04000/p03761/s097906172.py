import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(IN())
mod=1000000007

#+++++

def main():
	n = int(input())
	#b , c = tin()
	tt = [1000]*30
	gi = lambda c : ord(c)-ord('a')
	for i in range(n):
		s = input()
		t = [0]*30
		for c in s:
			t[gi(c)]+=1
		for i, (tn, ttn) in enumerate(zip(t, tt)):
			tt[i] = min(tn, ttn)
			
	v = ['']*30
	for i, n in enumerate(tt):
		o = chr(i+ord('a'))
		v[i] = o*n
	ret = ''.join(v)
	print(ret)
	
	
	
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