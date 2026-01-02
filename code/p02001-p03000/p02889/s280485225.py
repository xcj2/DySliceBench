import sys,collections as cl,bisect as bs
Max = 10**18
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())

def wa(d):
    for k in range(len(d)):
        for i in range(len(d)):
            for j in range(len(d)):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    return d

def on():
    N,M,L = m()

    e = [[Max for i in range(N)]for j in range(N)]

    for i in range(M):
        a,b,c = m()
        e[a-1][b-1] = c
        e[b-1][a-1] = c

    for i in range(N):
        e[i][i] = 0

    d = wa(e)


    E = [[Max for i in range(N)]for j in range(N)]

    for i in range(N):
        for j in range(N):
            if d[i][j] <= L:
                E[i][j] = 1

    for i in range(N):
        E[i][i] = 0

    E = wa(E)
    q = onem()
    for i in range(q):
        s,t = m()
        if E[s-1][t-1] == Max:
            print(-1)
        else:
            print(E[s-1][t-1]-1)

if __name__ == "__main__":
    on()


