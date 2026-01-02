import sys
def I(): return int(sys.stdin.readline())
def LI(): return [int(x) for x in sys.stdin.readline().split()]

N,M,V,P = LI()
A = LI()
A.sort()

def check(x):
    if (N-x)<=P:
        return True
    x_score = A[x] + M
    if (V-x-P) <= 0:
        return(A[N-P]<=x_score)

    total_v = (V-x-P)*M

    if(A[N-P]>x_score):
        return False

    for i in range(x+1,N-P+1):
        total_v -= min(M,(x_score - A[i]))
    if(total_v>0):
        return False
    return True

def main():
    if(check(0)):
        print(N)
        return

    isOK = N-1
    isNG = 0
    while(isOK-isNG>1):
        mid = (isOK+isNG)//2
        if(check(mid)):
            isOK = mid
        else:
            isNG = mid
    print(N-isOK)
    return


if __name__ == "__main__":
    main()

