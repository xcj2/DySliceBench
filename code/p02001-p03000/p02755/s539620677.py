
#####

import numpy as np
from numpy import newaxis, float32, float64, int32, int64, int16, int8, uint8, uint32, complex64, complex128

#####

def getIntList(inp):
	return [int(_) for _ in inp]


from sys import stdin
import sys

def getInputs():
	inputs=[]
	for line in stdin:
		line=line.split()
		inputs.append(line)
	return inputs


def main(inputs):
	a8,b10=getIntList(inputs[0])
	
	min8=int(np.ceil(a8/0.08))
	max8=int(a8/0.08+12)
	min10=b10*10
	max10=b10*10+9
	
	for i8 in range(min8, max8+1):
		if i8>=min10 and i8<=max10:
			print(i8)
			sys.exit(0)
	print(-1)

if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)
	
