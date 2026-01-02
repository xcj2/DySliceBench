import sys

use_clipboard=True
bbn=1000000007
	
#+++++

		
def main():
	n,m,x_c,y_c = map(int, input().split())
	xl=list(map(int, input().split()))
	yl=list(map(int, input().split()))
	xl.append(x_c)
	yl.append(y_c)
	#pa(xl)
	#pa(yl)
	if max(xl)+1 <= min(yl):
		print('No War')
	else:
		print('War')
	return 
	
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
			#sys.stdin=clipboard.get()
		else:
			sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)