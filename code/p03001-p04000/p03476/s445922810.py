from math import sqrt
from bisect import bisect_right

def eratos(n):
    L = [True for _ in range(n+1)]
    L[0],L[1] = False,False

    for i in range(2,int(sqrt(n))+1):
        if L[i]:
            for j in range(2,n//i+1):
                L[i*j] = False

    P = []
    for i in range(n+1):
        if L[i]:
            P.append(i)

    return P

def sim(P):
    #よく考えたら元の数より小さい数に対する判定
    #なのでisPrime関数を使うまでもない
    P_set = set(P)
    P_sim = []
    for i in range(len(P)):
        if (P[i]+1)//2 in P_set:
            P_sim.append(P[i])

    return P_sim

def main():
    Q = int(input())

    P = eratos(10**5)
    P_sim = sim(P)

    ans_L = []
    for i in range(Q):
        l,r = map(int,input().split())
        ans = bisect_right(P_sim,r)-bisect_right(P_sim,l-1)
        ans_L.append(ans)

    for i in range(Q):
        print(ans_L[i])

if __name__ == "__main__":
    main()
