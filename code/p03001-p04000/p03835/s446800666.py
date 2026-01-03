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
    k, s = MI()

    cnt = 0
    for x in range(0, k + 1):
        for y in range(0, k + 1):
            z = s - x - y
            if z < 0 or z > k:
                continue
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()
