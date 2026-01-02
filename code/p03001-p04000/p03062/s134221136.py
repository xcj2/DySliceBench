import sys,bisect,heapq

mod = 10**9+7

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(input())

def GCD(a,b):
    while(a%b != 0):
        a,b = b,a%b
    return b

def LCM(a,b):
    return a*b//GCD(a,b)

def main():
    N = I()
    A = LI()

    count_m = 0
    for a in A:
        if a < 0:
            count_m += 1
    A_abs = [abs(a) for a in A]

    if count_m %2 == 0:
        return(sum(A_abs))
    else:
        return(sum(A_abs)-2*(min(A_abs)))

if __name__ == "__main__":
    print(main())
