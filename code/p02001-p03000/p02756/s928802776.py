
from sys import stdin
import sys

def getInputs():
	inputs=[]
	for line in stdin:
		line=line.split()
		inputs.append(line)
	return inputs

def rev(s):
	return s[-1::-1]

# def main(inputs):
# 	s=inputs[0][0]
# 	q=int(inputs[1][0])
# 
# 	for qi in range(q):
# 		ti=int(inputs[qi+2][0])
# 		if ti==1:
# 			s=rev(s)
# 		else:
# 			f=int(inputs[qi+2][1])
# 			c=inputs[qi+2][2]
# 			if f==1:
# 				s=c+s
# 			else:
# 				s=s+c
# 	print(s)


class E:
	def __init__(self, c, pre, nex):
		self.c=c
		self.pre=pre
		self.nex=nex
		

	
def main(inputs):
	s=inputs[0][0]
	q=int(inputs[1][0])
	
	prev=None
	for ci,c in enumerate(s):
		e=E(c, prev, None)
		if prev is not None: prev.nex=e
		prev=e
		if ci==0:
			head=e
	tail=e
	
	size=len(s)
	order=0 #0: forward, 1: backward
	for qi in range(q):
		ti=int(inputs[qi+2][0])
		if ti==1:
			order=1-order
		else:
			f=int(inputs[qi+2][1])
			c=inputs[qi+2][2]
			e=E(c, None, None)
			size+=1
			if f==1:
				if order==0:
					e.nex=head
					head.pre=e
					head=e
				else:
					e.pre=tail
					tail.nex=e
					tail=e
			else:
				if order==1:
					e.nex=head
					head.pre=e
					head=e
				else:
					e.pre=tail
					tail.nex=e
					tail=e
	
	cList=[None]*size
	if order==0:
		e=head
		for i in range(size):
			cList[i]=e.c
			e=e.nex
	else:
		e=tail
		for i in range(size):
			cList[i]=e.c
			e=e.pre
	
	print("".join(cList))
	

if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)
	
