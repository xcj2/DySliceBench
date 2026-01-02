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

from collections import deque
def solve():
    n = II()
    H = LI()

    d = deque()

    def split_0(lst):
        res = []
        tmp = []
        for l in lst:
            if l == 0:
                if len(tmp) > 0:
                    res.append(tmp)
                    tmp = []
            else:
                tmp.append(l)
        if len(tmp) > 0:
            res.append(tmp)
        return res

    r = split_0(H)
    d.extend(r)
    # print(d)

    cnt = 0
    while len(d) > 0:
        lst = d.popleft()
        mn = min(lst)
        res = split_0(list(map(lambda x: x - mn, lst)))
        cnt += mn
        d.extend(res)
    print(cnt)




if __name__ == '__main__':
    solve()
