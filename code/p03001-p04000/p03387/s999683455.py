import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    X=list(mi())

    X.sort()

    ans = 0
    while X[1] != X[2]:
        X[0] += 1
        X[1] += 1
        ans += 1
    
    if X[0] == X[1]:
        print(ans)
        exit()
    
    if X[0] % 2 == X[1] % 2:
        ans += (X[1] - X[0])//2
    else:
        ans += (X[1]+1 - X[0])//2
        ans += 1
    
    print(ans)







if __name__ == "__main__":
    main()