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
    ans = False

    for i in route[n]:
        if 1 in route[i]:
            ans = True
    print("POSSIBLE" if ans else "IMPOSSIBLE")
        

main()            
