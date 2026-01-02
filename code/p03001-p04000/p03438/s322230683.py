import sys

use_clipboard=False
bbn=1000000007
	
#+++++

		
def main():
	n = int(input())
	bl = list(map(int, input().split()))
	cl = list(map(int, input().split()))
	
	dd = sum([max(c-b,0) for b,c in zip(bl,cl)])
	pp = sum([max(b-c,0) for b,c in zip(bl, cl)])
	
	ss=sum([(c-b) % 2 for b,c in zip(bl,cl) if c >= b])
	pa(('dd',dd,'pp',pp))
	if (dd - ss)< pp*2:
		return 'No'
	
	return 'Yes'
	
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