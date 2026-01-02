

from sys import stdin
import sys
sys.setrecursionlimit(10**8)

def getInputs():
	inputs=[]
	for line in stdin:
		line=line.split()
		inputs.append(line)
	return inputs

def r(x):
	return x[::-1]


def main(inputs):
	s=inputs[0][0]
	n=len(s)
	if s[::-1]!=s:
		print("No")
		sys.exit(0)
# 	print(s[0:(n-1)//2])
	if s[0:(n-1)//2]!=r(s[0:(n-1)//2]):
		print("No")
		sys.exit(0)
# 	print(s[(n+3)//2-1:])
	if s[(n+3)//2-1:]!=r(s[(n+3)//2-1:]):
		print("No")
		sys.exit(0)
	print("Yes")
	
	

if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)

