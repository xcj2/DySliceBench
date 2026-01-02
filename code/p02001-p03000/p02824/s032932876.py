import sys
def I(): return int(sys.stdin.readline())
def LI(): return [int(x) for x in sys.stdin.readline().split()]

def check(x,N,M,V,P,A):
    if (N-x)<=P:
        return True
    if(V<=x+P):
        return(A[x]+M>=A[N-P])

    x_score = A[x]+M
    total_v = (V-x-P)*M

    if(A[N-P]>x_score):
        return False

    for i in range(x+1,N-P+1):
        total_v -= min(M,(x_score - A[i]))
    if total_v <= 0:
        return True
    else:
        return False

def main():
    N,M,V,P = map(int,input().split())
    A = [int(x) for x in input().split()]
    A.sort()

    if(check(0,N,M,V,P,A)):
        print(N)
        return

    isOK = N-1
    isNG = 0
    while(isOK-isNG>1):
        middle = (isOK+isNG)//2
        if(check(middle,N,M,V,P,A)):
            isOK = middle
        else:
            isNG = middle
    print(N-isOK)
    return


if __name__ == "__main__":
    main()

