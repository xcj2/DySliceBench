import sys
sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

INF = float('inf')

def solve():
    S = list(input())
    # print(S)

    # 最初を書き換えない
    iro = S[0]
    cnt1 = 0
    for idx, s in enumerate(S):
        if idx % 2 == 0 and s != iro:
            cnt1 += 1
        elif idx % 2 != 0 and s == iro:
            cnt1 += 1

    # 最初を書き換える
    cnt2 = 0
    for idx, s in enumerate(S):
        if idx % 2 == 0 and s == iro:
            cnt2 += 1
        elif idx % 2 != 0 and s != iro:
            cnt2 += 1

    print(min(cnt1, cnt2))



if __name__ == '__main__':
    solve()
