import sys
from collections import defaultdict

use_clipboard=True
bbn=1000000007
	
#+++++

		
def main():
	n = int(input())
	al = list(map(int, input().split()))
	
	cc=defaultdict(lambda : 0)
	for v in al:
		cc[v] += 1
		
	ccl=[]
	for key in cc:
		ccl.append((key,cc[key]))
	ccl.sort(reverse=True)
	
	ma,mb=0,0
	for v,n in ccl:
		if ma == 0 and n >= 4:
			return v*v
		elif ma == 0 and n >= 2:
			ma = v
		elif n >= 2:
			return ma*v
	return 0
	
	
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