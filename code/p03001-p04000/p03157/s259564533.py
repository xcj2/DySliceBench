import sys,bisect,heapq

mod = 10**9+7

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(list(sys.stdin.readline())[:-1])

def GCD(a,b):
    while(a%b != 0):
        a,b = b,a%b
    return b

def LCM(a,b):
    return a*b//GCD(a,b)

def main():
    H,W = LI()
    a = [[c=="#" for c in S()] for _ in range(H)]
    b = [[True for _ in range(W)] for _ in range(H)]

    r = 0
    for h in range(H):
        for w in range(W):
            if b[h][w]:
                q = []
                T = 0
                F = 0
                q.append([a[h][w],h,w])
                while(q):
                    flag,h_s,w_s = q.pop()
                    if b[h_s][w_s] and a[h_s][w_s] == flag:
                        if flag:
                            T += 1
                        else:
                            F += 1
                        b[h_s][w_s] = False
                        for i in [[-1,0],[1,0],[0,-1],[0,1]]:
                            if 0<=h_s+i[0]<=H-1 and 0<=w_s+i[1]<=W-1 and b[h_s+i[0]][w_s+i[1]]:
                                q.append([not(flag),h_s+i[0],w_s+i[1]])
                r += T*F
    return r




if __name__ == "__main__":
    print(main())
