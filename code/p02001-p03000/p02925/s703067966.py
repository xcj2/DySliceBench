import sys
sys.setrecursionlimit(10 ** 7)


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def main():
    N = int(input())
    X = [[] for i in range(N)]
    for i in range(N):
        for j in LI():
            X[i].append(j-1)
        X[i].reverse()

    Q = []
    def check(i):
        if len(X[i])==0:
            return
        j = X[i][-1]
        if len(X[j])==0:
            return
        if i==X[j][-1]:
            if i<j:
                Q.append((i,j))
            else:
                Q.append((j,i))

    for i in range(N):
        check(i)

    day = 0
    while len(Q)>0:
        day += 1
        Q.sort()
        Q = list(set(Q))
        prevQ = Q.copy()
        Q = []
        for i,j in prevQ:
            X[i].pop()
            X[j].pop()
        for i,j in prevQ:
            check(i)
            check(j)

    for i in range(N):
        if len(X[i])>0:
            print("-1")
            return

    print(day)
    return

main()