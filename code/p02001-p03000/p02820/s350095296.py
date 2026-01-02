import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,k=map(int, input().split())
    r,s,p=map(int, input().split())
    t=input()
    def kachip(te):
        if te=='r':
            return p
        elif te=='s':
            return r
        else:
            return s
    def kachite(te):
        if te == 'r':
            return 'p'
        elif te == 's':
            return 'r'
        else:
            return 's'

    check=[0]*k # 出した手
    ans=0
    for i in range(n):
        point=kachip(t[i])
        te=kachite(t[i])
        if check[i%k]==te:
            check[i%k]=0
        else:
            ans+=point
            check[i%k]=te
    print(ans)
resolve()