import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
LIN=lambda : list(IN())
mod=1000000007

#+++++

class dd:
	def __init__(self, k):
		d='zzzzzz'
		self.v = [d]*k
		#self.v[0]='a'
		#pa(self.v)
		
	def add(self, v):
		if v in self.v:
			pass
		elif self.v[-1] <= v:
			pass
		else:
			for i,c in enumerate(self.v):
				if v < c:
					self.v = self.v[:i]+[v]+self.v[i:-1]
					break
		#pa((v, self.v))
				
	def get(self):
		return self.v[-1]


def main():
	#a = int(input())
	#b , c = IN()
	s = input()
	k = int(input())
	rs=dd(k)
	for i in range(1, 5+1):
		for j in range(len(s)-i+1):
			v = s[j:j+i]
			rs.add(v)
			
	r=rs.get()
	print(r)
	
	
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