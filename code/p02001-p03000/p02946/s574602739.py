import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    K,X = mi()
    Z = list(range(2000001))

    x = X
    ans = set()
    for i in range(K):
        y1 = x + i 
        y2 = x - i

        for y in [y1,y2]:
            y += 1000000
            if 0<= y < len(Z):
                ans.add(y-1000000)

    ans = list(ans)
    ans.sort()

    print(*ans,sep=" ")





if __name__ == "__main__":
    main()