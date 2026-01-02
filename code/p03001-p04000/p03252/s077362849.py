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
    S = list(input())
    T = list(input())

    ds = {}
    dt = {}
    ids = ''
    idt = ''
    cids = 0
    cidt = 0
    for i in range(len(S)):
        # S
        s = S[i]
        if s in ds:     # 出現済みの文字なら、その文字のIDを追加する
            idss = ds[s]
            ids = ids + str(idss)
        else:           # 新たに出現した文字なら、新しいIDを追加し、メモしておく
            cids += 1
            ds[s] = cids
            ids = ids + str(cids)

        # T
        t = T[i]
        if t in dt:
            idst = dt[t]
            idt = idt + str(idst)
        else:
            cidt += 1
            dt[t] = cidt
            idt = idt + str(cidt)

        if ids != idt:
            print('No')
            return

    print('Yes')



if __name__ == '__main__':
    solve()
