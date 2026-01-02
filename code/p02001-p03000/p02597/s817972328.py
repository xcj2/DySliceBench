import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    C = list(input())

    R = []
    W = []
    for i,c in enumerate(C):
        if c == "R":
            R.append(i)
        else:
            W.append(i)
    

    W.sort(reverse=True)
    R.sort()

    if len(R) == 0 or len(W) == 0:
        print(0)
        exit()

    ri = R.pop()
    wi = W.pop()

    ans = 0
    while not ri < wi:
        ans += 1
        if len(R) == 0 or len(W) == 0: break

        ri = R.pop()
        wi = W.pop()    


    print(ans)






if __name__ == "__main__":
    main()