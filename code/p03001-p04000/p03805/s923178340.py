import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    n,m = LI()
    root = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = LI()
        root[a].append(b)
        root[b].append(a)

    pers = itertools.permutations(list(range(2,n+1)))
    ans = 0

    for per in pers:
        for i in range(n-1):
            if i == 0:
                now = 1
                next = per[0]
                if next not in root[now]:
                    break
            else:
                now = per[i-1]
                next = per[i]
                if next not in root[now]:
                    break
        else:
            ans += 1
    
    print(ans)
main()