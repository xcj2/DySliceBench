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

def dfs(lst, cnt):

    sub = []
    min_ = INF
    # print(lst, cnt, sub, min_)
    for l in lst:
        if l == 0:
            if min_ != INF:
                # print(min_, sub)
                cnt += min_
                cnt = dfs(list(map(lambda x: x-min_, sub)) + [0], cnt)
                sub = []
                min_ = INF
            else:
                continue
        else:
            min_ = min(min_, l)
            sub.append(l)
    # print('a')
    return cnt

def solve():
    n = II()
    H = LI()

    ans = dfs(H + [0], cnt=0)
    print(ans)

if __name__ == '__main__':
    solve()
