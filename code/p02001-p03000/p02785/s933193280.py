import sys

use_clipboard=False
bbn=1000000007
	
#+++++

		
def main():
	n,k = map(int, input().split())
	hl=list(map(int, input().split()))
	hl.sort()
	#pa(hl)
	if k > 0:
		ret = sum(hl[:-k])
	else:
		ret=sum(hl)
	print(ret)
	
	
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