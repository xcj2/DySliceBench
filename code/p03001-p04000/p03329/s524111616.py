import sys
sys.setrecursionlimit(10**6) 

def memorize(f):
    table = {}
    def func(*args):
        if not args in table:
            table[args] = f(*args)
        return table[args]
    return func

@memorize
def memDFS(n):
    if n==0:
        return 0
    else:
        res = n
        pow6 = 1
        while(pow6<=n):
            res = min(res, memDFS(n-pow6)+1)
            pow6 *= 6
        pow9 = 1
        while(pow9<=n):
            res = min(res, memDFS(n-pow9)+1)
            pow9 *= 9
        return res

N = int(input())
print(memDFS(N))