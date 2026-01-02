import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	S = sys.stdin.readline()

	counter = 0
	if(S[0]!='k'):
		if(S[-8:-1]=='keyence'):
			print("YES")
		else:
			print("NO")
	elif(S[0]=="k" and S[-2]!="e"):
		if(S[0:7]=='keyence'):
			print("YES")
		else:
			print("NO")
	elif(S[0]=="k" and S[-2]=="e"):
		key = "keyence"
		f = False
		for i in range(1,7):
			if(key == str(S[0:i])+str(S[-8+i:-1])):
				print("YES")
				f = True
				break
		if f==False : print("NO")
	else:
		print("NO")

main()