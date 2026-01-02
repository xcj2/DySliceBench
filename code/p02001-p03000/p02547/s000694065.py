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
        x,y=mi()
        X.append((x,y))
    
    count = 0
    for i in range(N):
        if X[i][0] == X[i][1]:
            count += 1
        else:
            count = 0
        
        if count >= 3:
            print("Yes")
            exit()
    
    print("No")





if __name__ == "__main__":
    main()