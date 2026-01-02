import sys

use_clipboard=True
bbn=1000000007
	
#+++++

class dd:
	def __init__(self, a_h):
		self.h=a_h

		
def main():
	h=int(input())
	ret = 0
	ec=1
	while h >= 1:
		ret += ec
		ec *= 2
		h = h // 2 
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