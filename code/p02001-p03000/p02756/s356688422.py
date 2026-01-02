import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
printV = lambda x: print(*x, sep="\n")
printH = lambda x: print(" ".join(map(str,x)))
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	S = IS()
	Q = II()
	c = 0
	head=[]
	tail=[]
	for _  in range(Q):
		query = IS()
		if(len(query)==1):
			c = (c + 1)%2
		else:
			T,F,C = query.split()
			T = int(T)
			F = int(F)
			if F==1:
				if(c==0):
					head.append(C)
				else:
					tail.append(C)
			else:
				if(c==1):
					head.append(C)
				else:
					tail.append(C)
	if c == 0:
		head = ''.join(head[::-1])
		tail = ''.join(tail)
		ans = head+S+tail
	else:
		head = ''.join(head)
		tail = "".join(tail[::-1])
		ns = S[::-1]
		ans = tail+ns+head
	print(ans)




if __name__ == '__main__':
	main()