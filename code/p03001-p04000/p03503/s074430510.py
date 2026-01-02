import sys
bbn=1000000007
	
#+++++

class store:
	def __init__(self, is_open):
		ret=0
		for i,v in enumerate(is_open):
			ret += (2**i)*v
		self.is_open=ret
	
	def add_proof_info(self,pl):
		self.ploofs=pl
		
	def get_proof(self, time):
		count=0
		temp=self.is_open
		tt=time
		while temp>0:
			count+=1&tt&temp
			tt=tt>>1
			temp=temp>>1
			#print(temp)

		return self.ploofs[count]
		
def main():
	n = int(input())
	stores=[]
	for i in range(n):
		is_open = list(map(int, input().split()))
		st=store(is_open)
		stores.append(st)
		
	for s in stores:
		pl=list(map(int, input().split()))
		s.add_proof_info(pl)
	
	ret=None
	for i in range(1,(2**10)+0):
		value=sum([s.get_proof(i) for s in stores])
		if ret is None or ret < value:
			ret = value
		
	print(ret)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)