from sys import stdin
input = stdin.readline

def solve():
    n,m = map(int,input().split())
    p = [tuple(map(int,inp.split())) for inp in stdin.read().splitlines()]
    father = [-1] * n
    count = n
    def getfather(x):
        if father[x] < 0: return x
        father[x] = getfather(father[x])
        return father[x]


    def union(x, y):
        x = getfather(x)
        y = getfather(y)
        nonlocal count
        if x != y:
            count -= 1
            if father[x] > father[y]:
                x,y = y,x
            father[x] += father[y]
            father[y] = x

    for a,b in p:
        union(a-1,b-1)
        
    print(count - 1)

if __name__ == '__main__':
    solve()