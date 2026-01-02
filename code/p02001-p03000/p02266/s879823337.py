import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    S = SS()
    stk = []
    pool_stk = []

    ans = 0
    for i, e in enumerate(S):
        if e=='\\':
            stk.append(i)
        elif e=='/':
            if stk:
                idx_d = stk.pop()
                pool_layer = i - idx_d
                ans += pool_layer
                if pool_stk and idx_d<pool_stk[-1][0]:
                    merged_pool = 0
                    while pool_stk and idx_d<pool_stk[-1][0]:
                        pool_tmp = pool_stk.pop()
                        merged_pool += pool_tmp[1]
                    pool_stk.append((idx_d, merged_pool+pool_layer))
                else:
                    pool_stk.append((idx_d, pool_layer))
    
    print(ans)
    print(len(pool_stk), *[i[1] for i in pool_stk])

if __name__ == '__main__':
    resolve()

