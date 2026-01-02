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

def printlist(lst, k='\n'): return k.join(list(map(str, lst)))
INF = float('inf')

def solve():
    n = II()
    A = LI()
    A = sorted(A)
    # print(A)
    # for _ in range(10):
    while 1:
        if len(set(A)) == 1:
            print(A[0])
            return

        a0 = A[0]
        for i in range(1, n):
            ai = A[i]
            if ai % a0 == 0:
                A[i] = a0
            else:
                A[i] = ai % a0
        A = sorted(A)
        # print(A)

if __name__ == '__main__':
    solve()
