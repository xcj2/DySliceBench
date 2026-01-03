import sys,bisect,heapq

mod = 10**9+7
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(input())
def IR(n): return([I() for _ in range(n)])

def GCD(a,b):
    while(a%b != 0):
        a,b = b,a%b
    return b

def LCM(a,b):
    return a*b//GCD(a,b)

def main():
    N,L = LI()
    A = LI()
    ans = "Impossible"

    for i in range(N-1):
        if A[i]+A[i+1] >= L:
            ans = "Possible"
            last = i+1
            break

    if ans == "Impossible":
        print(ans)
    else:
        print(ans)
        for i in range(1,last):
            print(i)
        for i in range(N-1,last,-1):
            print(i)
        print(last)







    

if __name__ == "__main__":
    main()
