import sys,heapq,bisect

mod = 10**9+7

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return input()

def GCD(a,b):
    while(a%b != 0):
        a,b = b,a%b
    return b

def LCM(a,b):
    return a*b//GCD(a,b)

def main():
    N = I()
    S1 = S()
    S2 = S()

    r = 1
    d_type = 0
    i = 0

    if S1[0] == S2[0]:
        r *= 3
        i += 1
        d_type = 0
    else:
        r *= 3 * 2
        i += 2
        d_type = 1

    while i < N:
        if d_type == 0 and S1[i] == S2[i]:
            r *= 2
            r %= mod
            d_type = 0
            i += 1
        elif d_type == 1 and S1[i] == S2[i]:
            d_type = 0
            i += 1
        elif d_type == 0 and S1[i] != S2[i]:
            r *= 2
            r %= mod
            d_type = 1
            i += 2
        else:
            r *= 3
            r %= mod
            d_type = 1
            i += 2

    return(r)

if __name__ == "__main__":
    print(main())