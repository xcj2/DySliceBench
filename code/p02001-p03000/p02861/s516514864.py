import itertools
import math
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    X = []
    for i in range(N):
        x,y = mi()
        X.append((x,y))

    sm = 0
    count = 0
    for v in itertools.permutations(X,N):
        V = list(v)
        pre = V[0]

        for u in V[1:]:
            d = math.sqrt((pre[0]-u[0])**2 + (pre[1]-u[1]) ** 2)
            sm += d
        
        count += 1

    ans = sm/count
    print('{:.10f}'.format(ans))

    


if __name__ == "__main__":
    main()