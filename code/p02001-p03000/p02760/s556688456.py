
#####

import numpy as np
from numpy import newaxis, float32, float64, int32, int64, int16, int8, uint8, uint32, complex64, complex128
import itertools

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

def v(on):
	for i in range(3):
		if on[i,:].all():
			return True
	for i in range(3):
		if on[:,i].all():
			return True
	
	if on[0,0] and on[1,1] and on[2,2]: return True
	if on[2,0] and on[1,1] and on[0,2]: return True
	return False

def main(inputs):
	a=np.empty((3,3),int32)
	aIndex={}
	on=np.zeros((3,3),np.bool)
	for i,j in itertools.product(range(3),range(3)):
		a[i,j]=int(inputs[i][j])
		aIndex[a[i,j]]=(i,j)
		
	n=int(inputs[3][0])
	for i in range(n):
		bi=int(inputs[i+4][0])
		if bi in aIndex:
			index=aIndex[bi]
			on[index[0],index[1]]=True
	
	vv=v(on)
	if vv: print("Yes")
	else: print("No")
	

if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)
	
