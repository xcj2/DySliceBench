import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,K=mi()
    G = []

    X=[]
    Y=[]
    for i in range(N):
        x,y = mi()
        G.append((x,y))
        X.append(x)
        Y.append(y)

    def count(downx,upx,downy,upy):
        _count = 0
        for i in range(N):
            x,y = G[i]
            if downx<=x<=upx and downy<=y<=upy:
                _count += 1
        
        return _count

    ans = INF
    for downx in X:
        for upx in X:
            if upx <= downx: continue
            for downy in Y:
                for upy in Y:
                    if upy <= downy: continue

                    if count(downx,upx,downy,upy) >= K:
                        ans = min(ans,abs(upx-downx) * abs(upy-downy))
                        



    print(ans)

            



if __name__ == "__main__":
    main()