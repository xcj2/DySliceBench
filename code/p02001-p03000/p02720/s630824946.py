import sys
import heapq

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
	k = II()
	a = [1,2,3,4,5,6,7,8,9]
	heapq.heapify(a)
	total = 0
	while(total!=k):
		i = heapq.heappop(a)
		total+=1
		li = i%10
		if(li%10==0):
			heapq.heappush(a,i*10+li)
			heapq.heappush(a,i*10+li+1)
		elif(li%10==9):
			heapq.heappush(a,i*10+li-1)
			heapq.heappush(a,i*10+li)
		else:
			heapq.heappush(a,i*10+li-1)
			heapq.heappush(a,i*10+li)
			heapq.heappush(a,i*10+li+1)
	print(i)

if __name__ == '__main__':
	main()