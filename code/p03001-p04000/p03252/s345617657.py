import sys

use_clipboard=True
bbn=1000000007
	
#+++++

def check(sc,tc):
	sc.sort()
	tc.sort()
	for u,v in zip(sc,tc):
		if len(u)!=len(v):
			return False
		for i,j in zip(u,v)	:
			if i!=j:
				return False
	return True
		
						
def main():
	s = input()
	t = input()
	c2i=lambda c : ord(c)-ord('a')
	sc=[[] for _ in range(26)]
	tc=[[] for _ in range(26)]
	
	for i,c in enumerate(s):
		#pa(c2i(c))
		sc[c2i(c)].append(i)
		
	for i,c in enumerate(t):
		tc[c2i(c)].append(i)
		
		
	ret = 'Yes' if check(sc,tc) else 'No'
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