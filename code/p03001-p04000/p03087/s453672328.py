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

INF = float('inf')

def solve():
    n, q = MI()
    S = input()
    ats = [0]
    cnt = 0
    for i in range(n-1):
        j = i + 2
        s = S[i:j]
        # print(s)
        if s == 'AC':
            cnt += 1
        ats.append(cnt)
    # print(ats)
    for _ in range(q):
        l, r = MI1()
        # print(S[l:r+1])
        print(ats[r] - ats[l])


if __name__ == '__main__':
    solve()
