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

    ans = 0
    for i in range(n+1):
        if i % 2 == 0: continue
        cnt = 1
        for j in range(2, i+1):
            if i % j: continue
            cnt += 1
        if cnt == 8:
            ans += 1
        # print(i, cnt)
    print(ans)



if __name__ == '__main__':
    solve()
