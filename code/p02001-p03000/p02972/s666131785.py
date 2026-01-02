import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

def solve():
    n = II()
    A = LI()

    B = [-1] * n
    for i in range(n, 0, -1):
        # print(i)
        s = 0
        for j in range(i+i, n+1, i):
            # print(f' {j}')
            s ^= B[j-1]
        B[i-1] = A[i-1] ^ s
    # print(B)

    print(sum(B))
    for idx, b in enumerate(B):
        if b: print(idx+1)


if __name__ == '__main__':
    solve()
