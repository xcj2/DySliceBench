import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    if N == 0:
        print(0)
        exit()

    ans = []
    while N != 1:
        # print(N)
        if N % 2 == 0:
            ans.append("0")
            q = N // (-2)
            N = q

        else:
            ans.append("1")
            q = (N-1) // (-2)
            N = q
        

    ans.append("1")
    print("".join(ans[::-1]))





if __name__ == "__main__":
    main()