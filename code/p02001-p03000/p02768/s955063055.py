import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def modinv(a,m):
	b=m
	u=1
	v=0
	
	while b > 0:
		t = a //b
		a = a - (t * b)
		a,b = b,a
		u = u - (t * v)
		u,v=v,u
	
	u = u % m
	if u < 0:
		u+=m
	return u

def cob(n,a):
	rr=1
	for i in range(n, n-a, -1):
		rr = (rr *i ) % mod
	
	r=1
	for i in range(1, a+1):
		r = (r *i ) % mod
	
	#ww=pow(r,-1,mod)
	ww=modinv(r, mod)
	ret = rr * ww
	return ret
	
	

def main():
	n, a , b = IN()
	
	mm=(pow(2,n,mod)-1)%mod
	ret=(mm-cob(n,a)-cob(n,b))%mod
	
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

