import sys

sys.setrecursionlimit(10 ** 6)
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]



def main():
    a=LI()
    n=a[0]
    x=a[1]-1
    y=a[2]-1
    dist={}
    ans={}
    for i in range(n):
        dist[i]={}
        ans[i]=0
    for i in range(n):
        for j in range(i+1, n):
            dist[i][j]=min(j-i, 1+abs(j-y)+abs(i-x))
            ans[dist[i][j]]+=1
    for i in range(1,n):
        print(ans[i])
main()
