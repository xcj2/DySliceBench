import sys
import heapq

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	N,M = MI()
	A = LI()
	A = list(map(lambda x : x*(-1), A))
	heapq.heapify(A)
	for i in range(M):
		discnt_price = (heapq.heappop(A) * -1)//2
		heapq.heappush(A,discnt_price*-1)
	print(sum(A)*-1)


main()