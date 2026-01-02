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

S = ['3', '5', '7']
n = II()
cnt = 0

def dfs(ns, cnt):
    for s in S:
        news = ''.join([ns, s])
        # print(news)
        if eval(news) > n:
            continue
        elif len(set(list(news))) != 3:
            # 3, 5, 7がそろっていない
            cnt = dfs(news, cnt)
        else:
            cnt += 1
            # print('yes', news, cnt)
            cnt = dfs(news, cnt)
    return cnt


def solve():

    ans = dfs('', 0)
    print(ans)



if __name__ == '__main__':
    solve()
