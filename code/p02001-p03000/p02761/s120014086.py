
#####

import numpy as np
from numpy import newaxis, float32, float64, int32, int64, int16, int8, uint8, uint32, complex64, complex128

#####

def getIntList(inp):
	return [int(_) for _ in inp]
	

from sys import stdin

def getInputs():
	inputs=[]
	for line in stdin:
		line=line.split()
		inputs.append(line)
	return inputs


def main(inputs):
	n=int(inputs[0][0])
	m=int(inputs[0][1])

	no=False
	
	dig=-np.ones(n, int32)
	for i in range(m):
		si=int(inputs[1+i][0])-1
		ci=int(inputs[1+i][1])
		
		if dig[si]==-1:
			dig[si]=ci
		elif dig[si]!=ci:
			no=True
			break
		
	if dig[0]==-1:
		if n==1:
			dig[0]=0
		else:
			dig[0]=1
	
	dig[dig==-1]=0
	
	if dig[0]==0 and n>1:
		no=True
	
	if no:
		print("-1")
	else:
		print("".join(map(str, dig)))
			
		
	
	
	

if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)
	
