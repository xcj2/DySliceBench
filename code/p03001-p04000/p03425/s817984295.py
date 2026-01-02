import itertools
from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N = ii()
    count = defaultdict(lambda:0)

    for i in range(N):
        s = input()
        count[s[0]] += 1

    ans =0
    X = []
    for x in ["M","A","R","C","H"]:
        if count[x] < 1: continue
        X.append(x)
    
    if len(X) < 3:
        print(0)
        exit()

    for V in itertools.combinations(X,3):
        U = list(V)
        res = 1
        for u in U:
            res *= count[u]
        
        ans += res


    print(ans)

        
     


if __name__ == "__main__":
    main()