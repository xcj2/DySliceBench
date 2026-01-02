import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,q = LI()
    root = [[] for _ in range(n+1)]
    quest = [0 for _ in range(n+1)]

    for _ in range(n-1):
        a,b = LI()
        root[a].append(b)
        root[b].append(a)
    
    for _ in range(q):
        p,x = LI()
        quest[p] += x

    stock = collections.deque([1])
    explored = set()

    while len(stock) != 0:
        next = stock.pop()
        explored.add(next)
        for i in root[next]:
            if i not in explored:
                stock.append(i)
                quest[i] += quest[next]
    print(*quest[1:])
main()