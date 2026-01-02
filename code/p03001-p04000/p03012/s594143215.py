import sys
#input = sys.stdin.readline

def io_generator():
	return input()
	
def ioByFile(fn='inputFile.txt'):
	with open(fn) as f:
		for line in f:
			yield line[:-1]

#+++++ +++++ +++++#
		
def main(a_io):
	n = int(a_io())
	ww=list(map(int, a_io().split()))
	
	ss=sum(ww)
	left=0
	min_diff = ss
	for i in ww:
		left+=i
		diff = abs((ss-left)-left)
		if diff < min_diff:
			min_diff=diff
		else:
			break
	
	print(min_diff)
	
	
#+++++ +++++ +++++#

if __name__ == "__main__":
	io= lambda : io_generator()
	if sys.platform =='ios':
		testInput=ioByFile()
		io=lambda : next(testInput)
	main(io)