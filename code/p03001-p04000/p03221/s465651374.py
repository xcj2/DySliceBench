import sys
sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

INF = float('inf')

def solve():
    n, m = MI()
    dct = {}
    for i in range(m):
        p, y = MI()
        dct.setdefault(p, [])
        dct[p].append((i, y))
    # print(dct)

    ans = ['' for _ in range(m)]
    for key, value in dct.items():
        st = sorted(value, key=lambda x: x[1])
        # print(st)
        for idx, (i, year) in enumerate(st):
            id = str(key).zfill(6) + str(idx+1).zfill(6)
            # print(id)
            ans[i] = id

    for iid in ans:
        print(iid)

if __name__ == '__main__':
    solve()
