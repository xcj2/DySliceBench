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
    S = list(input())

    acgt = ['A', 'G', 'C', 'T']
    cnt = 0
    ans = 0
    for s in S:
        if s in acgt:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    print(max(ans, cnt))


if __name__ == '__main__':
    solve()
