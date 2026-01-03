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
	a,b,c=MI()
	ta,tb,tc=a,b,c
	ch = False
	cnt = 0
	while a%2==0 and b%2==0 and c%2==0:
		a,b,c=1/2*(b+c),1/2*(a+c),1/2*(b+a)
		if(a==ta and b==tb and c==tc):
			ch = True
			break
		cnt+=1
	if ch:
		print(-1)
	else:
		print(cnt)


if __name__ == '__main__':
	main()