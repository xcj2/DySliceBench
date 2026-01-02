import sys

use_clipboard=True
bbn=1000000007
	
#+++++

		
def main():
	h, n = map(int, input().split())
	ii=[]
	for i in range(n):
		a,b=map(int, input().split())
		ii.append([a/b, a, b])
	#ii.sort()
	
	_,ma,mb = ii[0]
	tn = (h + ma-1)//ma
	tc = tn * mb
	
	vv=[bbn]*(h+1)
	vv[0]=0
	for i in range(h+1):
		for c,a,b in ii:
			nn = min(i + a, h)
			vv[nn]= min(vv[i] + b, vv[nn])
	
	print(vv[-1])
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
class input_clipboard:
	def __init__(self,s):
		self.input_l=s.splitlines()
		self.ii=0
		
	def input(self):
		ret = self.input_l[self.ii]
		self.ii+=1
		return ret

if __name__ == "__main__":
	if sys.platform =='ios':
		if use_clipboard:
			import clipboard
			input_text=clipboard.get()
			ic=input_clipboard(input_text)
			input = lambda : ic.input()
		else:
			sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)