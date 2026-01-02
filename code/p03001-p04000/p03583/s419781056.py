import sys

input_methods=['clipboard','file','key']
input_method=input_methods[1]

bbn=1000000007
	
#+++++

def check(n,h,j):
	#aa = 4*h*j*w - n*h*j - n*j*w - n*w*h
	#aa==0 => 4hjw-njw-nwh == nhj
	t= (4*h*j-n*j-n*h)
	if t!=0 and n*h*j % t == 0:
		#pa((t, n*h*j))
		return (n*h*j)//t
	return -1
	
	#return (4/n)-(1/h + 1/j + 1/w)

		
def main():
	n = int(input())
	#4/N==1/h+1/j+1/w
	#2h==j==w => 4/N==4/2h
	#N = 2h
	
	#4hjw==N(hj+jw+wh)
	#N==4(hjw)/(hj+jw+wh)
	for h in range(1,3501):
		for j in range(1,3501):
			w = check(n,h,j)
			if w > 0:
				#pa(4/n)
				#pa((1/h)+(1/j)+(1/w))
				return ' '.join([str(v) for v in [h,j,w]])
			continue
			
			
			
			#for w in range(1,3501):
			if check(n,h,j,1) > 0:
				break
			if check(n,h,j,3500)<0:
				break
			if check(n,h,j,1)==0:
				return (h,j,1)
			if check(n,h,j,3500)==0:
				return (h,j,3500)
			ok=3500
			ng=0
			while ok-ng>1:
				mid = (ok+ng)//2
				cc= check(n,h,j,mid)
				if cc == 0:
					return (h,j,mid)
				elif cc < 0:
					ng=mid
				else:
					ok=mid
				#print(h,j,w)
	
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