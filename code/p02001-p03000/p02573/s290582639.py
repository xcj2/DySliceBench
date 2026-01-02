import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,m = LI()
    route = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = LI()
        route[a].append(b)
        route[b].append(a)
    explored = set()

    sstock = collections.deque([i for i in range(1,n+1)])
    ans = 0
    while len(sstock)!=0:
        nnext = sstock.pop()
        if nnext not in explored:
            cnt = 0
            stock = collections.deque([nnext])
            explored.add(nnext)
            while len(stock) != 0:
                next = stock.pop()
                cnt += 1   
                for i in route[next]:
                    if i not in explored:
                        stock.append(i)
                        explored.add(i)
            ans = max(ans,cnt)
    print(ans)
main()            
