import sys

sys.setrecursionlimit(10 ** 6)
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]



def main():
    m=LI()
    k=m[0]
    n=m[1]
    a=LI()
    for i in range(n):
        if i!=0:
            a[i]-=a[0]
    a[0]=0;
    ans=k;
    for i in range(n-1):
        ans=min(ans, k-(a[i+1]-a[i]))
    ans=min(ans, a[n-1])
    print(ans)
main()
