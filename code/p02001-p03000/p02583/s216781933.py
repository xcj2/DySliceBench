import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    L=list(mi())

    ans = 0
    for i in range(N):
        for j in range(i,N):
            if i == j: continue
            for k in range(j,N):
                if j == k: continue
                a,b,c = L[i],L[j],L[k]
                if a != b  and b != c and c != a:
                    if a+b>c and  b+c>a and  c+a>b:
                        ans += 1

    print(ans)




if __name__ == "__main__":
    main()